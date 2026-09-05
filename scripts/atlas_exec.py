#!/usr/bin/env python3
"""
Atlas Digital — Executor Unificado
Executa ações no trowinstore e ofertasamazon via REST API
Reduz copy/paste: execute apenas os scripts pré-definidos.
"""
import json, sys, os, base64
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


# ============== AÇÕES ==============

def list_plugins(site_key):
    c = load_config()
    site = c["sites"][site_key]
    plugins = request(site, "wp/v2/plugins?per_page=100")
    if isinstance(plugins, dict) and "error" in plugins:
        print(f"Erro: HTTP {plugins['error']}")
        return
    print(f"\n=== {site_key} — {len(plugins)} plugins ===")
    for p in plugins:
        s = "ATIVO" if p.get("status") == "active" else "inativo"
        print(f"  [{s}] {p['name']} v{p['version']}")


def list_posts(site_key):
    c = load_config()
    site = c["sites"][site_key]
    posts = request(site, "wp/v2/posts?per_page=10")
    if isinstance(posts, dict) and "error" in posts:
        print(f"Erro: HTTP {posts['error']}")
        return
    print(f"\n=== {site_key} — {len(posts)} posts ===")
    for p in posts:
        print(f"  ID {p['id']}: {p['title']['rendered']}")


def update_tagline(site_key, tagline):
    c = load_config()
    site = c["sites"][site_key]
    r = request(site, "wp/v2/settings", "PUT", {"description": tagline})
    if "error" in r:
        print(f"Erro: {r['message']}")
    else:
        print(f"Tagline atualizada: {r.get('description', tagline)}")


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


def list_pretty_links(site_key):
    c = load_config()
    site = c["sites"][site_key]
    links = request(site, "pretty-links/v1/links")
    if isinstance(links, dict) and "error" in links:
        print(f"Erro: HTTP {links['error']}")
        return
    print(f"\n=== {site_key} — {len(links)} links ===")
    for link in links:
        print(f"  ID {link['id']}: {link.get('name', 'Sem nome')}")
        print(f"     Slug: {link.get('slug', 'N/A')}")
        print(f"     URL:  {link.get('url', 'N/A')[:80]}")


# ============== MENU ==============

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python atlas_exec.py <acao> [site] [args]")
        print("Acoes disponiveis:")
        print("  plugins  - Listar plugins ativos/inativos")
        print("  posts    - Listar posts publicados")
        print("  links    - Listar Pretty Links")
        print("  tagline  - Atualizar tagline do site")
        print("  css      - Injetar CSS customizado")
        print("Sites: trowinstore, ofertasamazon")
        sys.exit(1)

    action = sys.argv[1]
    site_key = sys.argv[2] if len(sys.argv) > 2 else "trowinstore"

    if action == "plugins":
        list_plugins(site_key)
    elif action == "posts":
        list_posts(site_key)
    elif action == "links":
        list_pretty_links(site_key)
    elif action == "tagline":
        tagline = sys.argv[3] if len(sys.argv) > 3 else "Atlas Digital"
        update_tagline(site_key, tagline)
    elif action == "css":
        css = sys.argv[3] if len(sys.argv) > 3 else "body{color:red}"
        inject_css(site_key, css)
    else:
        print(f"Acao desconhecida: {action}")
        print("Acoes: plugins, posts, links, tagline, css")
