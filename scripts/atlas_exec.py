#!/usr/bin/env python3
"""
Atlas Digital — Executor Unificado (Expandido)
Executa ações no trowinstore e ofertasamazon via REST API
"""
import json, sys, base64
import urllib.request
import urllib.error
from pathlib import Path

CONFIG = Path(__file__).parent.parent / "config" / "sites.local.json"


def load_config():
    with open(CONFIG, encoding="utf-8") as f:
        return json.load(f)


def auth(site):
    return base64.b64encode(
        f"{site['username']}:{site['application_password']}".encode()
    ).decode()


def request(site, endpoint, method="GET", data=None):
    url = f"{site['url']}/wp-json/{endpoint}"
    headers = {
        "Authorization": f"Basic {auth(site)}",
        "Content-Type": "application/json"
    }
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {"error": e.code, "message": e.read().decode()[:200]}
    except Exception as e:
        return {"error": "exception", "message": str(e)[:200]}


# ============== AÇÕES DE LISTAGEM ==============

def list_plugins(site_key):
    c = load_config()
    site = c["sites"][site_key]
    plugins = request(site, "wp/v2/plugins?per_page=100")
    if isinstance(plugins, dict) and "error" in plugins:
        print(f"Erro: HTTP {plugins['error']}")
        return
    ativos = [p for p in plugins if p.get("status") == "active"]
    inativos = [p for p in plugins if p.get("status") != "active"]
    print(f"\n=== {site_key} — {len(plugins)} plugins ({len(ativos)} ativos) ===")
    for p in ativos:
        print(f"  [ATIVO]   {p['name']} v{p['version']}")
    for p in inativos:
        print(f"  [inativo] {p['name']} v{p['version']}")


def list_posts(site_key):
    c = load_config()
    site = c["sites"][site_key]
    posts = request(site, "wp/v2/posts?per_page=100")
    if isinstance(posts, dict) and "error" in posts:
        print(f"Erro: HTTP {posts['error']}")
        return
    print(f"\n=== {site_key} — {len(posts)} posts ===")
    for p in posts:
        status = p.get("status", "?")
        title = p.get("title", {}).get("rendered", "Sem titulo")
        print(f"  ID {p['id']}: {title} [{status}]")


def list_pages(site_key):
    c = load_config()
    site = c["sites"][site_key]
    pages = request(site, "wp/v2/pages?per_page=100")
    if isinstance(pages, dict) and "error" in pages:
        print(f"Erro: HTTP {pages['error']}")
        return
    print(f"\n=== {site_key} — {len(pages)} paginas ===")
    for p in pages:
        print(f"  ID {p['id']}: {p['title']['rendered']} (slug: {p.get('slug', '?')})")


def list_pretty_links(site_key):
    c = load_config()
    site = c["sites"][site_key]
    links = request(site, "pretty-links/v1/links")
    if isinstance(links, dict) and "error" in links:
        print(f"Erro: HTTP {links['error']}")
        return
    print(f"\n=== {site_key} — {len(links)} links ===")
    for link in links:
        name = link.get("name", "Sem nome")
        slug = link.get("slug", "N/A")
        url = link.get("url", "N/A")
        clicks = link.get("clicks", 0)
        print(f"  ID {link['id']}: {name}")
        print(f"     Slug: {slug} | Clicks: {clicks}")
        print(f"     URL:  {url[:80]}")


def list_categories(site_key):
    c = load_config()
    site = c["sites"][site_key]
    cats = request(site, "wp/v2/categories?per_page=50")
    if isinstance(cats, dict) and "error" in cats:
        print(f"Erro: HTTP {cats['error']}")
        return
    print(f"\n=== {site_key} — {len(cats)} categorias ===")
    for cat in cats:
        print(f"  ID {cat['id']}: {cat['name']} ({cat.get('count', 0)} posts)")


# ============== AÇÕES DE CRIAÇÃO ==============

def create_post(site_key, title, content):
    c = load_config()
    site = c["sites"][site_key]
    data = {
        "title": title,
        "content": content,
        "status": "publish"
    }
    r = request(site, "wp/v2/posts", "POST", data)
    if "error" in r:
        print(f"Erro: {r['message']}")
    else:
        print(f"Post criado: ID {r['id']} — {r['title']['rendered']}")
        print(f"   Link: {r['link']}")


def create_pretty_link(site_key, name, url):
    c = load_config()
    site = c["sites"][site_key]
    data = {
        "url": url,
        "name": name,
        "cloaking": "1"
    }
    r = request(site, "pretty-links/v1/links", "POST", data)
    if "error" in r:
        print(f"Erro: {r['message']}")
    else:
        print(f"Link criado: ID {r['id']} — {r['slug']}")
        print(f"   URL: {r['url'][:80]}")


# ============== AÇÕES DE ATUALIZAÇÃO ==============

def update_tagline(site_key, tagline):
    c = load_config()
    site = c["sites"][site_key]
    r = request(site, "wp/v2/settings", "PUT", {"description": tagline})
    if "error" in r:
        print(f"Erro: {r['message']}")
    else:
        print(f"Tagline atualizada: {r.get('description', tagline)}")


def update_post(site_key, post_id, title=None, content=None, status=None):
    c = load_config()
    site = c["sites"][site_key]
    data = {}
    if title:
        data["title"] = title
    if content:
        data["content"] = content
    if status:
        data["status"] = status
    if not data:
        print("Nenhum campo para atualizar")
        return
    r = request(site, f"wp/v2/posts/{post_id}", "POST", data)
    if "error" in r:
        print(f"Erro: {r['message']}")
    else:
        print(f"Post {post_id} atualizado: {r['title']['rendered']} [{r['status']}]")


# ============== AÇÕES DE EXCLUSÃO ==============

def delete_post(site_key, post_id, force=False):
    c = load_config()
    site = c["sites"][site_key]
    # Verificar se o post existe
    r = request(site, f"wp/v2/posts/{post_id}")
    if isinstance(r, dict) and "error" in r:
        print(f"Erro: Post {post_id} nao encontrado")
        return
    title = r.get("title", {}).get("rendered", "?")
    if not force:
        print(f"Post encontrado: ID {post_id} — {title}")
        print(f"Use --force para confirmar exclusao")
        return
    # Excluir (DELETE) ou mover para lixeira (status: trash)
    delete_resp = request(site, f"wp/v2/posts/{post_id}", "DELETE")
    if "error" in delete_resp:
        # Tentar mover para lixeira
        trash_resp = request(site, f"wp/v2/posts/{post_id}", "POST", {"status": "trash"})
        if "error" in trash_resp:
            print(f"Erro: {trash_resp['message']}")
        else:
            print(f"Post {post_id} movido para lixeira: {title}")
    else:
        print(f"Post {post_id} excluido permanentemente: {title}")


def delete_pretty_link(site_key, link_id, force=False):
    c = load_config()
    site = c["sites"][site_key]
    # Buscar link
    r = request(site, f"pretty-links/v1/links/{link_id}")
    if isinstance(r, dict) and "error" in r:
        print(f"Erro: Link {link_id} nao encontrado")
        return
    name = r.get("name", "?")
    if not force:
        print(f"Link encontrado: ID {link_id} — {name}")
        print(f"Use --force para confirmar exclusao")
        return
    delete_resp = request(site, f"pretty-links/v1/links/{link_id}", "DELETE")
    if "error" in delete_resp:
        print(f"Erro: {delete_resp['message']}")
    else:
        print(f"Link {link_id} excluido: {name}")


# ============== AÇÕES DE INJEÇÃO ==============

def inject_css(site_key, css_code):
    c = load_config()
    site = c["sites"][site_key]
    data = {
        "title": f"Atlas CSS — {site_key}",
        "code": css_code,
        "type": "css",
        "status": "active"
    }
    r = request(site, "wp/v2/wpcode-snippets", "POST", data)
    if "error" in r:
        print(f"WPCode nao disponivel: HTTP {r['error']}")
    else:
        print(f"CSS injetado (ID: {r['id']})")


# ============== DIAGNÓSTICO ==============

def diagnostic(site_key):
    c = load_config()
    site = c["sites"][site_key]

    print(f"\n=== Diagnostico: {site_key} ===")
    print(f"URL: {site['url']}")
    print(f"Usuario: {site['username']}")

    # Testar autenticacao
    r = request(site, "wp/v2/users/me")
    if isinstance(r, dict) and "error" in r:
        print(f"Autenticacao: FALHOU (HTTP {r['error']})")
        return
    print(f"Autenticacao: OK (User ID {r.get('id')})")

    # Contar posts
    posts = request(site, "wp/v2/posts?per_page=1")
    if isinstance(posts, dict) and "error" in posts:
        total_posts = "?"
    else:
        total_posts = len(posts)
    print(f"Posts (pagina 1): {total_posts}")

    # Contar paginas
    pages = request(site, "wp/v2/pages?per_page=1")
    if isinstance(pages, dict) and "error" in pages:
        total_pages = "?"
    else:
        total_pages = len(pages)
    print(f"Paginas (pagina 1): {total_pages}")

    # Contar plugins ativos
    plugins = request(site, "wp/v2/plugins?per_page=100")
    if isinstance(plugins, dict) and "error" in plugins:
        print(f"Plugins: erro ao listar")
    else:
        ativos = sum(1 for p in plugins if p.get("status") == "active")
        print(f"Plugins: {len(plugins)} total, {ativos} ativos")

    # Pretty Links
    links = request(site, "pretty-links/v1/links")
    if isinstance(links, dict) and "error" in links:
        print(f"Pretty Links: nao disponivel")
    else:
        print(f"Pretty Links: {len(links)} links criados")


# ============== MENU PRINCIPAL ==============

ACTIONS = {
    "plugins": "Listar plugins (uso: plugins <site>)",
    "posts": "Listar posts (uso: posts <site>)",
    "pages": "Listar paginas (uso: pages <site>)",
    "links": "Listar Pretty Links (uso: links <site>)",
    "categories": "Listar categorias (uso: categories <site>)",
    "diagnostic": "Diagnostico completo do site (uso: diagnostic <site>)",
    "create-post": "Criar post (uso: create-post <site> <titulo> <conteudo>)",
    "create-link": "Criar Pretty Link (uso: create-link <site> <nome> <url>)",
    "update-post": "Atualizar post (uso: update-post <site> <id> [titulo] [conteudo] [status])",
    "delete-post": "Mover/excluir post (uso: delete-post <site> <id> [--force])",
    "delete-link": "Excluir Pretty Link (uso: delete-link <site> <id> [--force])",
    "tagline": "Atualizar tagline (uso: tagline <site> <texto>)",
    "css": "Injetar CSS (uso: css <site> <codigo_css>)",
}


def show_help():
    print("=" * 60)
    print("Atlas Digital — Executor Unificado (v2.0)")
    print("=" * 60)
    print("Uso: python atlas_exec.py <acao> [site] [args...]")
    print()
    print("Acoes disponiveis:")
    for action, desc in ACTIONS.items():
        print(f"  {action:18} {desc}")
    print()
    print("Sites: trowinstore, ofertasamazon")
    print()
    print("Exemplos:")
    print("  atlas plugins ofertasamazon")
    print("  atlas posts trowinstore")
    print("  atlas delete-post trowinstore 313 --force")
    print("  atlas create-post trowinstore 'Titulo' 'Conteudo aqui'")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        show_help()
        sys.exit(0)

    action = sys.argv[1]
    site_key = sys.argv[2] if len(sys.argv) > 2 else "trowinstore"

    # Detectar flag --force
    args = sys.argv[3:]
    force = "--force" in args
    if force:
        args.remove("--force")

    # ============== ROTEAMENTO ==============

    if action == "plugins":
        list_plugins(site_key)
    elif action == "posts":
        list_posts(site_key)
    elif action == "pages":
        list_pages(site_key)
    elif action == "links":
        list_pretty_links(site_key)
    elif action == "categories":
        list_categories(site_key)
    elif action == "diagnostic":
        diagnostic(site_key)
    elif action == "create-post":
        if len(args) < 2:
            print("Uso: create-post <site> <titulo> <conteudo>")
            sys.exit(1)
        create_post(site_key, args[0], args[1])
    elif action == "create-link":
        if len(args) < 2:
            print("Uso: create-link <site> <nome> <url>")
            sys.exit(1)
        create_pretty_link(site_key, args[0], args[1])
    elif action == "update-post":
        if len(args) < 1:
            print("Uso: update-post <site> <id> [titulo] [conteudo] [status]")
            sys.exit(1)
        post_id = args[0]
        title = args[1] if len(args) > 1 else None
        content = args[2] if len(args) > 2 else None
        status = args[3] if len(args) > 3 else None
        update_post(site_key, post_id, title, content, status)
    elif action == "delete-post":
        if len(args) < 1:
            print("Uso: delete-post <site> <id> [--force]")
            sys.exit(1)
        delete_post(site_key, args[0], force=force)
    elif action == "delete-link":
        if len(args) < 1:
            print("Uso: delete-link <site> <id> [--force]")
            sys.exit(1)
        delete_pretty_link(site_key, args[0], force=force)
    elif action == "tagline":
        tagline = " ".join(args) if args else "Atlas Digital"
        update_tagline(site_key, tagline)
    elif action == "css":
        css = " ".join(args) if args else "body{color:red}"
        inject_css(site_key, css)
    else:
        print(f"Acao desconhecida: {action}")
        print(f"Use 'help' para ver acoes disponiveis")
        sys.exit(1)
