# Atlas Digital - Status Atual

**Última atualização:** 2026-09-06

## Estado do Repositório

**Branch atual:** main (origin/main sincronizado)

### Arquivos Modificados Localmente (NÃO commitados)
- apps/AtlasBootstrap/config/config.json
- apps/AtlasBootstrap/modules/ConfigManager.ps1
- apps/AtlasBootstrap/modules/Logger.ps1
- apps/AtlasBootstrap/modules/Validator.ps1
- apps/AtlasBootstrap/modules/Workspace.ps1
- apps/AtlasBootstrap/src/AtlasBootstrap.ps1

### Arquivos Novos (não versionados)
- scripts/atlas_apply_visual.py
- scripts/atlas_update_pages.py
- scripts/css_trowin.css
- scripts/_test_apply.py
- docs/resumo_atlas.txt

---

## Estado dos Sites (2026-09-06)

### trowinstore.com.br
- **Status:** Ativo
- **URL:** https://trowinstore.com.br
- **Tema:** Standard Pro
- **API:** HTTP 200
- **Email admin:** trowinstore@gmail.com
- **Idioma:** pt_BR
- **Usuário API:** Equipe TROWIN (ID: 10)
- **Título:** TROWIN STORE
- **Tagline:** Marketing de Afiliados | Tutoriais YouTube | Empreendedorismo Digital
- **Logo:** trowin_logo.jpg (72.6 KB) - site_logo + site_icon (favicon)

### Páginas (6)
| ID | Slug | Título | Conteúdo |
|----|------|--------|----------|
| 25 | about | Sobre Nós | 920 chars |
| 29 | contact | Contato | 2.531 chars (formulário) |
| 31 | disclosure | Disclosure | 882 chars |
| 33 | privacy-policy | Política de Privacidade | 2.702 chars |
| 35 | terms-of-use | Termos de Uso | 1.904 chars |
| 317 | home | Home | 1.455 chars |

### Posts (4)
| ID | Título | Categoria | Imagem | CTA |
|----|--------|-----------|---------|-----|
| 314 | Bem-vindo a TROWIN STORE! | Marketing Digital (44) | Sim | Conheça o Projeto |
| 328 | Marketing de Afiliados: Como Começar em 2026 | Marketing Digital (44) | Sim | Ver Ofertas Amazon |
| 329 | Tutoriais YouTube: Monetize seu Canal | Marketing Digital (44) | Sim | Assistir no YouTube |
| 330 | Empreendedorismo Digital: Guia para Iniciantes | Marketing Digital (44) | Sim | Saiba Mais |

### ofertasamazon.trowinstore.com.br
- **Status:** Ativo
- **URL:** https://ofertasamazon.trowinstore.com.br
- **Tema:** Astra
- **API:** HTTP 200
- **Email admin:** trowin2@gmail.com
- **Usuário API:** atlas-api (ID: 2)
- **Plugins ativos (16):** Wordfence, WooCommerce, Pretty Links, All in One SEO, Elementor, Spectra, LiteSpeed Cache, Site Kit, OttoKit, WPForms, IA Hostinger, Astra Widgets, Starter Templates, Hostinger Tools, etc.

### Páginas (4)
| ID | Slug | Título |
|----|------|--------|
| 1008 | home | Home |
| 1004 | contact | Contact |
| 1002 | about | About |
| 6, 7, 8, 9 | shop, cart, checkout, my-account | WooCommerce |

### Posts (4)
| ID | Título |
|----|--------|
| 1 | Bem-vindo ao OfertaAmazon! |
| 2073 | Melhores Cadeiras Gamer Ergonômicas com Desconto |
| 2074 | Fones de Ouvido Noise Cancelling com Oferta Imperdível |
| 2075 | Cortador de Cabelo Elétrico Profissional - Oferta Limitada |

### Links de Afiliado UTM (Pretty Links v4.0.14)
| ID | Produto | Slug | Post | UTM |
|----|---------|------|------|-----|
| 9 | Cadeira Ergonômica Gamer | /a4aq | ID 2073 | Sim |
| 10 | Fone Noise Cancelling | /bkzr | ID 2074 | Sim |
| 11 | Cortador de Cabelo Elétrico | /ah12 | ID 2075 | Sim |

**Parâmetros UTM:** `utm_source=ofertasamazon`, `utm_medium=affiliate`, `utm_campaign=produtos-amazon`

---

## Identidade Visual TROWIN (Aplicada)

### Paleta de Cores
| Cor | Hex | Uso |
|-----|-----|-----|
| Fundo principal | #f0f4f8 | Background geral |
| Fundo escuro | #1A2238 | Header e footer |
| Ciano | #00E5FF | Destaques, links hover, gradientes |
| Roxo | #B026FF | Botões, hover, gradientes |
| Branco | #ffffff | Textos no escuro, posts |
| Cinza escuro | #2a2a2a | Texto principal |

### Elementos Aplicados
- Header com gradiente ciano/roxo sobre fundo escuro
- Título com gradiente de texto ciano→roxo
- Logo à esquerda + Título + Menu à direita
- Slogan abaixo do título (subtítulo)
- Posts centralizados (max-width: 900px)
- Botões com gradiente ciano→roxo e texto escuro (contraste correto)
- Footer com borda superior roxa
- Widgets com borda ciano
- Esconder "Por atlas-api" (agora "Por Equipe TROWIN")
- Esconder datas nos posts
- Imagens centralizadas
- Responsivo (mobile)

### Status de Aplicação
- CSS injetado via WPCode Lite (manual)
- API REST do WPCode Lite não disponível (HTTP 404)

---

## Segurança e Autenticação

### Application Passwords
- Usuário `Equipe TROWIN` criado em ambos os sites
- Senhas armazenadas em `config/sites.local.json` (protegido pelo .gitignore)
- Autenticação REST API validada via endpoint `/wp/v2/users/me`
- Novas senhas geradas via script (`scripts/atlas_exec.py`)

### Status de Segurança
- .gitignore protege credenciais locais
- Wordfence Security v8.1.4 ativo no ofertasamazon
- Páginas WooCommerce únicas (sem duplicatas)
- Posts recategorizados (de "Videos" para "Marketing Digital")
- Autor renomeado para "Equipe TROWIN"

---

## Scripts do Projeto (`scripts/`)

### `atlas_exec.py` (v2.1)
Executor unificado com 14 ações (plugins, posts, pages, links, categories, diagnostic, create-post, create-link, update-post, delete-post, delete-link, tagline, css, theme)

### `atlas_apply_visual.py`
Aplica identidade visual TROWIN. Gera CSS para aplicação manual.

### `atlas_update_pages.py`
Atualiza páginas PT-BR com formulários e conteúdo LGPD.

### `css_trowin.css`
CSS final consolidado para aplicação manual no WPCode Lite.

---

## Atalhos (Aliases)

### PowerShell
```powershell
function atlas { python K:/Projetos/atlas-digital/scripts/atlas_exec.py @args }
Set-Alias -Name atlas -Value atlas
```

### Uso
```powershell
atlas plugins ofertasamazon
atlas posts trowinstore
atlas pages trowinstore
atlas diagnostic ofertasamazon
atlas links ofertasamazon
```

---

## Resumo Geral do Projeto

| Área | Status |
|------|--------|
| Estrutura do Repositório | Monorepo completo |
| Documentação | 5 arquivos principais em `docs/` |
| trowinstore.com.br | Ativo, 4 posts, 6 páginas |
| ofertasamazon.trowinstore.com.br | Ativo, 4 posts, 3 links UTM |
| Identidade Visual TROWIN | Aplicada (cor, tipografia, layout) |
| Segurança | Wordfence ativo, App Passwords protegidas |
| Plugins | WooCommerce, Pretty Links, WPCode Lite |
| Scripts | 3 ferramentas Python |
| GitHub | Sincronizado |

### Commits à frente do origin
Total: 15+ commits locais ainda não enviados ao origin.

---

## Próximas Ações (Pós-Projeto)

1. **Revogar Application Passwords antigas** no painel WordPress de cada site
2. **Push para origin/main** para sincronizar todos os commits
3. **Configurar WooCommerce** (moeda, métodos de pagamento) no ofertasamazon
4. **Configurar AIOSEO** para otimização de SEO
5. **Publicar mais conteúdo** (posts regulares)
6. **Monitorar conversões** de afiliados
7. **Considerar tema GeneratePress** (substituir Standard Pro)
