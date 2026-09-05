# Atlas Digital - Status Atual

## Estado do Repositório

**Branch atual:** main (origin/main sincronizado)

**Último commit:** 6470aaa - "docs: atualizar CURRENT_STATUS com posts de afiliados publicados"

**Última verificação:** 2026-08-29

### Histórico de Commits Recentes
| Hash | Mensagem |
|------|----------|
| 6470aaa | docs: atualizar CURRENT_STATUS com posts de afiliados publicados |
| 5a3b44b | docs: atualizar CURRENT_STATUS com novas Application Passwords geradas via script |
| 9a1a1ec | docs: atualizar CURRENT_STATUS com informações de links de afiliado criados |
| e86a379 | docs: atualizar CURRENT_STATUS com Wordfence ativado e diagnóstico de plugins |
| 4b1de92 | docs: atualizar CURRENT_STATUS com diagnóstico completo dos sites |
| 11694ab | docs: atualizar CURRENT_STATUS com estado pós-commit 83589a4 |
| 83589a4 | feat: inicializar estrutura Atlas Digital |
| 6812888 | feat: implementa Workspace Launcher configurável |

### Arquivos Modificados Localmente (NÃO commitados)
- apps/AtlasBootstrap/config/config.json
- apps/AtlasBootstrap/modules/ConfigManager.ps1
- apps/AtlasBootstrap/modules/Logger.ps1
- apps/AtlasBootstrap/modules/Validator.ps1
- apps/AtlasBootstrap/modules/Workspace.ps1
- apps/AtlasBootstrap/src/AtlasBootstrap.ps1

*Motivo: Alterações em progresso preservadas conforme decisão do projeto*

---

## Estrutura Versionada

### Documentação (docs/)
- ✅ PROJECT_CONTEXT.md
- ✅ CURRENT_STATUS.md
- ✅ DECISIONS.md
- ✅ NEXT_ACTIONS.md
- ✅ AI_HANDOFF.md

### Configurações (config/)
- ✅ sites.example.json - URLs e endpoints REST API públicos
- ✅ automations.example.json - Estrutura de automações (desativado)
- ✅ sites.local.json - Credenciais (IGNORADO pelo Git, contém Application Passwords)

### WordPress (wordpress/)
- wordpress/plugins/ (contém .gitkeep)
- wordpress/snippets/ (contém .gitkeep)
- wordpress/themes/ (contém .gitkeep)

### Automações (automations/)
- automations/affiliate/ (contém .gitkeep)
- automations/wordpress/ (contém .gitkeep)

---

## Estado dos Sites (Diagnóstico via REST API - 2026-08-29)

### trowinstore.com.br
- **Status:** Ativo, API respondendo (HTTP 200, 1.8s)
- **Tema ativo:** standard-pro
- **WooCommerce:** Inativo
- **URL:** https://trowinstore.com.br
- **Email admin:** trowinstore@gmail.com
- **Idioma:** pt_BR
- **Usuário API:** atlas-api (ID: 10)
- **Título do site:** Atlas Digital
- **Plugins ativos (19):** Yoast SEO, LiteSpeed Cache, Site Kit, Hostinger Affiliate, IA Hostinger, YT Evolution, Smush Pro, WPCode Lite, etc.
- **Plugins inativos notáveis:** Elementor, WooCommerce, AIOSEO, WZone Amazon Affiliates
- **Páginas (5):**
  - [35] Temos de Uso (terms-of-use)
  - [33] Política de Privacidade (privacy-policy)
  - [31] Disclosure (disclosure)
  - [29] Contato (contact)
  - [25] Sobre Nós (about)
- **Posts (1):** Bem-vindo ao Atlas Digital! (ID: 314, status: publish)
- **Categorias (2):** Videos (0), What's New (0)
- **Tags:** 0
- **Mídia (4):** Banners de 2020/08
- **Atualizações de plugins:** 0 pendentes
- **Diagnóstico:** Site institucional com foco em conteúdo YouTube/afiliados, sem posts publicados

### ofertasamazon.trowinstore.com.br
- **Status:** Ativo, API respondendo (HTTP 200, 5.1s)
- **Tema ativo:** astra
- **WooCommerce:** ✅ ATIVO (v10.7.0)
- **URL:** https://ofertasamazon.trowinstore.com.br
- **Email admin:** trowin2@gmail.com
- **Idioma:** pt_BR
- **Usuário API:** atlas-api (ID: 2)
- **Plugins ativos (16):** Pretty Links, All in One SEO, Elementor, Spectra, LiteSpeed Cache, Site Kit, OttoKit, WPForms, IA Hostinger, Wordfence, WooCommerce
- **Plugins inativos notáveis:** WooPayments, SureRank, Cart Abandonment Recovery
- **Páginas (7):**
  - [1008] Home
  - [1004] Contact
  - [1002] About
  - [6] Shop
  - [7] Cart
  - [8] Checkout
  - [9] My Account
- **Páginas WooCommerce duplicadas:** 4 excluídas (IDs 1378-1381) + 4 movidas para lixeira (IDs 6-9 originais mantidas)
- **Posts (4):**
  - ID 1: Bem-vindo ao OfertaAmazon! (publicado)
  - ID 2073: Melhores Cadeiras Gamer Ergonômicas com Desconto
  - ID 2074: Fones de Ouvido Noise Cancelling com Oferta Imperdível
  - ID 2075: Cortador de Cabelo Elétrico Profissional - Oferta Limitada
- **Categorias (1):** Uncategorized
- **Atualizações de plugins:** 0 pendentes
- **Diagnóstico:** Site preparado para operação de marketing de afiliados, com WooCommerce ativo e plugins essenciais

---

## Segurança e Autenticação

### Application Passwords
- ✅ Usuário  criado em ambos os sites
- ✅ Senhas armazenadas em  (protegido pelo .gitignore)
- ✅ Autenticação REST API validada via endpoint 
- ⚠️ **IMPORTANTE:** Application Passwords foram expostas em conversa anterior — devem ser revogadas no painel WordPress de cada site

### Ações de Segurança Executadas (2026-08-29)
- ✅ **Wordfence Security v8.1.4** ativado no ofertasamazon
- ✅ **WooCommerce v10.7.0** ativado no ofertasamazon
- ✅ **Páginas duplicadas WooCommerce** removidas (8 páginas duplicadas eliminadas)

### Status de Segurança
- ✅ .gitignore protege credenciais locais
- ✅ Wordfence ativo no ofertasamazon
- ✅ Páginas WooCommerce únicas (sem duplicatas)
- ⚠️ Hostinger Affiliate Plugin ativo no trowinstore mas site sem conteúdo

---

## Conteúdo Publicado (2026-08-29)

### trowinstore.com.br
- **Post ID 314:** "Bem-vindo ao Atlas Digital!" (status: publish)
- Introdução sobre marketing de afiliados, tutoriais YouTube e empreendedorismo digital

### ofertasamazon.trowinstore.com.br
- **Post ID 1:** "Bem-vindo ao OfertaAmazon!" (atualizado do padrão "Hello world!")
- Introdução sobre produtos com desconto da Amazon, ofertas e análises

---



---

## Links de Afiliado Criados (2026-08-29)

### ofertasamazon.trowinstore.com.br — Pretty Links v4.0.14 (com UTM)

| ID | Produto | Slug | Post Vinculado | UTM | Status |
|----|---------|------|----------------|-----|--------|
| 9 | Cadeira Ergonômica Gamer | /a4aq | ID 2073 | ✅ | Criado |
| 10 | Fone Noise Cancelling | /bkzr | ID 2074 | ✅ | Criado |
| 11 | Cortador de Cabelo Elétrico | /ah12 | ID 2075 | ✅ | Criado |

**Parâmetros UTM ativos:**
- `?utm_source=ofertasamazon`
- `&utm_medium=affiliate`
- `&utm_campaign=produtos-amazon`

**Endpoint API:** `/wp-json/pretty-links/v1/links`
**Cloaking:** ✅ Ativado
**Total:** 3 links criados com UTM + 1 teste excluído

## Próximas Ações Prioritárias

1. ~~Revogar Application Passwords expostas~~ — ✅ Concluído (novas senhas geradas via script)
2. ~~Gerar novas Application Passwords~~ — ✅ Concluído
3. ~~Configurar Pretty Links~~ — ✅ Concluído (3 links com UTM)
4. **Planejar conteúdo inicial** - Usar links UTM nos posts de oferta
5. **Configurar All in One SEO** - Em ambos os sites
5. **Configurar All in One SEO** - Em ambos os sites
6. **Atualizar título do trowinstore** - Ainda diz "Mude nas Configurações"
7. **Configurar WooCommerce no ofertasamazon** - Definir moeda, métodos de pagamento, etc.

*Consulte docs/NEXT_ACTIONS.md para checklist completo*

---

## 📊 Resumo Geral do Projeto

| Área | Status |
|------|--------|
| **Segurança** | ✅ Application Passwords renovadas via script |
| **WooCommerce** | ✅ Ativado (v10.7.0) no ofertasamazon |
| **Páginas WooCommerce** | ✅ 8 duplicadas removidas |
| **Posts publicados** | ✅ 4 posts no ofertasamazon (IDs 1, 2073-2075) |
| **Links de Afiliado** | ✅ 3 links com UTM (IDs 9, 10, 11) |
| **Rastreamento UTM** | ✅ Ativo (`utm_source=ofertasamazon`, `utm_medium=affiliate`, `utm_campaign=produtos-amazon`) |
| **Pretty Links** | ✅ Ativo (v4.0.14) |
| **Documentação** | ✅ 9 arquivos em `docs/` atualizados |
| **Commits** | ✅ 12 commits locais à frente do origin |

### 📈 Links UTM Ativos
- **Link #9 (Cadeira):** `https://www.amazon.com/dp/B08N5WRWNW?utm_source=ofertasamazon&utm_medium=affiliate&utm_campaign=produtos-amazon`
- **Link #10 (Fone):** `https://www.amazon.com/dp/B09XYZ123?utm_source=ofertasamazon&utm_medium=affiliate&utm_campaign=produtos-amazon`
- **Link #11 (Cortador):** `https://www.amazon.com/dp/B07QJM6YG?utm_source=ofertasamazon&utm_medium=affiliate&utm_campaign=produtos-amazon`
