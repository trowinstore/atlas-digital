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


# ============== INJEÇÃO DE TEMA COMPLETO ==============

def inject_full_theme(site_key):
    """Injeta CSS moderno + cria/atualiza home page visual (sem duplicacao)"""
    c = load_config()
    site = c["sites"][site_key]
    print(f"\n=== Customizando visual completo: {site_key} ===")

    # CSS moderno (tema Atlas Digital) - versao compacta
    css = """
/* === ATLAS DIGITAL — VISUAL COMPLETO === */
body{font-family:'Segoe UI',Roboto,sans-serif!important;background:#f5f7fa!important;color:#2c3e50!important}
.site-header,.header{background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%)!important;padding:18px 0!important;box-shadow:0 2px 10px rgba(0,0,0,0.1)!important}
.site-title a,.site-name a{color:#fff!important;font-size:28px!important;font-weight:700!important;text-decoration:none!important}
.site-description{color:#c5c6c7!important;font-size:14px!important}
nav.main-navigation,.main-nav,.primary-menu{background:transparent!important;margin-top:10px!important}
nav a,.menu a,.main-nav a{color:#fff!important;font-weight:500!important;padding:8px 16px!important;transition:color 0.3s!important}
nav a:hover,.menu a:hover{color:#e94560!important}
.content-area,.site-content{background:#fff!important;padding:30px!important;border-radius:12px!important;box-shadow:0 2px 8px rgba(0,0,0,0.05)!important;margin:20px auto!important;max-width:1200px!important}
.entry-title,.post-title,h2.post-title a,h1.post-title{color:#e94560!important;font-size:24px!important;margin-bottom:15px!important}
.entry-content,.post-content,.post{line-height:1.8!important;color:#2c3e50!important;font-size:16px!important}
.entry-content a,.post-content a{color:#e94560!important;text-decoration:none!important;font-weight:600!important}
.entry-content a:hover,.post-content a:hover{text-decoration:underline!important}
button,.button,input[type="submit"],.wp-block-button__link{background:#e94560!important;color:#fff!important;border-radius:6px!important;padding:10px 20px!important;border:none!important;font-weight:600!important;cursor:pointer!important;transition:background 0.3s!important}
button:hover,.button:hover,input[type="submit"]:hover{background:#c23850!important}
.widget,.sidebar .widget{background:#f8f9fa!important;border-radius:8px!important;padding:20px!important;margin-bottom:20px!important}
.widget-title,.widgettitle{color:#1a1a2e!important;font-size:18px!important;font-weight:700!important;margin-bottom:15px!important;border-bottom:2px solid #e94560!important;padding-bottom:8px!important}
footer,.site-footer,.footer{background:#0f3460!important;color:#fff!important;padding:40px 20px!important;text-align:center!important}
footer a,.site-footer a{color:#c5c6c7!important;text-decoration:none!important}
footer a:hover,.site-footer a:hover{color:#e94560!important}
@media (max-width:768px){.site-title a,.site-name a{font-size:22px!important}.content-area{padding:20px!important;margin:10px!important}.entry-title{font-size:20px!important}}
"""

    # 1. Verificar e tentar ativar WPCode
    plugins_resp = request(site, "wp/v2/plugins?per_page=100")
    wpcode_active = False
    wpcode_plugin = None
    if isinstance(plugins_resp, list):
        for p in plugins_resp:
            if not isinstance(p, dict):
                continue
            plugin_name = (p.get("name") or "")
            if isinstance(plugin_name, dict):
                plugin_name = plugin_name.get("raw", "")
            plugin_path = (p.get("plugin") or "").lower()
            if ("code" in plugin_name.lower() or "wpcode" in plugin_name.lower() or
                "code" in plugin_path or "insert-headers" in plugin_path):
                wpcode_plugin = p.get("plugin")
                if p.get("status") == "active":
                    wpcode_active = True
                    break
                else:
                    # Tentar ativar
                    try:
                        activate_resp = request(site, f"wp/v2/plugins/{wpcode_plugin}", "POST", {"status": "active"})
                        if isinstance(activate_resp, dict) and "error" not in activate_resp:
                            wpcode_active = True
                            print(f"[OK] Plugin '{plugin_name}' ativado")
                            break
                    except Exception:
                        pass

    # 2. Injetar CSS via WPCode (se ativo)
    css_injected = False
    if wpcode_active:
        data = {
            "title": f"Atlas Digital — Visual Theme",
            "code": css,
            "type": "css",
            "status": "active"
        }
        r = request(site, "wp/v2/wpcode-snippets", "POST", data)
        if isinstance(r, dict) and "error" in r:
            print(f"[AVISO] WPCode API nao disponivel (HTTP {r.get('error', '?')})")
            print("   WPCode Lite nao expoe endpoint REST - aplicar CSS via wp-admin")
        else:
            print(f"[OK] CSS moderno injetado (ID: {r.get('id', '?')})")
            css_injected = True
    else:
        print("[AVISO] WPCode nao disponivel - CSS nao injetado")

    # 3. Verificar se ja existe uma Home page (slugs: home, home-2, home-3, home-4, home-5, home-6)
    home_page = None
    pages_resp = request(site, "wp/v2/pages?per_page=100")
    if isinstance(pages_resp, list):
        for p in pages_resp:
            if not isinstance(p, dict):
                continue
            slug = (p.get("slug") or "").lower()
            title_rendered = (p.get("title") or {}).get("rendered", "")
            if "home" in slug.lower() or "home" in title_rendered.lower():
                if home_page is None or p.get("id", 999) < home_page.get("id", 999):
                    home_page = p

    home_content = "<header style=\"text-align:center;padding:60px 20px;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);color:#fff;border-radius:12px;margin-bottom:40px;\"><h1 style=\"font-size:48px;margin-bottom:20px;color:#fff;font-weight:700;\">Atlas Digital</h1><p style=\"font-size:20px;color:#c5c6c7;margin-bottom:30px;\">Marketing de Afiliados, Tutoriais YouTube, Empreendedorismo Digital</p><a href=\"/sobre-nos\" style=\"display:inline-block;padding:15px 40px;background:#e94560;color:#fff;text-decoration:none;border-radius:8px;font-weight:600;\">Conhecer Mais</a></header><section style=\"display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:30px;\"><div style=\"background:#fff;padding:30px;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,0.08);\"><h3 style=\"color:#e94560;margin-bottom:15px;\">Marketing de Afiliados</h3><p>Estrategias comprovadas para gerar renda com programas de afiliados.</p></div><div style=\"background:#fff;padding:30px;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,0.08);\"><h3 style=\"color:#e94560;margin-bottom:15px;\">Tutoriais YouTube</h3><p>Conteudo educativo sobre como criar e monetizar canais no YouTube.</p></div><div style=\"background:#fff;padding:30px;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,0.08);\"><h3 style=\"color:#e94560;margin-bottom:15px;\">Empreendedorismo</h3><p>Dicas e ferramentas para construir seu negocio digital do zero.</p></div></section>"

    if home_page:
        # Atualizar Home existente
        home_id = home_page.get("id", "?")
        home_slug = home_page.get("slug", "?")
        print(f"[INFO] Home page ja existe (ID {home_id}, slug: {home_slug}) - atualizando...")
        r = request(site, f"wp/v2/pages/{home_id}", "POST", {"content": home_content})
        if isinstance(r, dict) and "error" in r:
            print(f"[ERRO] Falha ao atualizar: {r.get('message', '?')[:100]}")
        else:
            print(f"[OK] Home page atualizada: ID {home_id}")
    else:
        # Criar nova Home page
        print("[INFO] Nenhuma Home page encontrada - criando nova...")
        data = {
            "title": "Home",
            "slug": "home",
            "status": "publish",
            "type": "page",
            "content": home_content,
            "excerpt": "Pagina inicial do Atlas Digital"
        }
        r = request(site, "wp/v2/pages", "POST", data)
        if isinstance(r, dict) and "error" in r:
            print(f"[ERRO] {r.get('message', '?')[:100]}")
        else:
            print(f"[OK] Home page criada: ID {r.get('id', '?')}")
            print(f"   Link: {r.get('link', '?')}")

    print(f"\n[OK] Customizacao completa: {site_key}")


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
    "theme": "Injetar tema completo (uso: theme <site>)",
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
    elif action == "theme":
        inject_full_theme(site_key)
    else:
        print(f"Acao desconhecida: {action}")
        print(f"Use 'help' para ver acoes disponiveis")
        sys.exit(1)
