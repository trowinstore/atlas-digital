# Atlas Digital - Status Atual

## Estado do Repositório

**Branch atual:** main (origin/main sincronizado)

**Último commit:** 4b1de92 - "docs: atualizar CURRENT_STATUS com diagnóstico completo dos sites"

**Última verificação:** 2026-08-29

### Histórico de Commits Recentes
| Hash | Mensagem |
|------|----------|
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
- **Plugins ativos (19):** Yoast SEO, LiteSpeed Cache, Site Kit, Hostinger Affiliate, IA Hostinger, YT Evolution, Smush Pro, WPCode Lite, etc.
- **Plugins inativos notáveis:** Elementor, WooCommerce, AIOSEO, WZone Amazon Affiliates
- **Páginas (5):**
  - [35] Temos de Uso (terms-of-use)
  - [33] Política de Privacidade (privacy-policy)
  - [31] Disclosure (disclosure)
  - [29] Contato (contact)
  - [25] Sobre Nós (about)
- **Posts:** 0 publicados
- **Categorias (2):** Videos (0), What's New (0)
- **Tags:** 0
- **Mídia (4):** Banners de 2020/08
- **Atualizações de plugins:** 0 pendentes
- **Diagnóstico:** Site institucional com foco em conteúdo YouTube/afiliados, sem posts publicados

### ofertasamazon.trowinstore.com.br
- **Status:** Ativo, API respondendo (HTTP 200, 5.1s)
- **Tema ativo:** astra
- **WooCommerce:** Inativo (páginas existem mas plugin desativado)
- **URL:** https://ofertasamazon.trowinstore.com.br
- **Email admin:** trowin2@gmail.com
- **Idioma:** pt_BR
- **Usuário API:** atlas-api (ID: 2)
- **Plugins ativos (15):** Pretty Links, All in One SEO, Elementor, Spectra, LiteSpeed Cache, Site Kit, OttoKit, WPForms, IA Hostinger, etc.
- **Plugins inativos notáveis:** WooCommerce, Wordfence (✅ **agora ATIVO**), WooPayments
- **Páginas (11):**
  - [1008] Home, [1004] Contact, [1002] About
  - [1378-1381] Shop, Cart, Checkout, My Account (recentes)
  - [6-9] Shop, Cart, Checkout, My Account (antigas - duplicadas)
- **Posts:** 1 (Hello world! padrão)
- **Categorias (1):** Uncategorized
- **Atualizações de plugins:** 0 pendentes
- **Diagnóstico:** Site preparado para marketing de afiliados (Pretty Links + AIOSEO), com Wordfence ativado para segurança

---

## Segurança e Autenticação

### Application Passwords
- ✅ Usuário  criado em ambos os sites
- ✅ Senhas armazenadas em  (protegido pelo .gitignore)
- ✅ Autenticação REST API validada via endpoint 
- ⚠️ **IMPORTANTE:** Application Passwords foram expostas em conversa anterior — devem ser revogadas no painel WordPress de cada site

### Status de Segurança
- ✅ .gitignore protege credenciais locais
- ✅ Wordfence ativado no ofertasamazon
- ⚠️ Páginas WooCommerce duplicadas no ofertasamazon (6-9 e 1378-1381) precisam limpeza
- ⚠️ Hostinger Affiliate Plugin ativo no trowinstore mas site sem conteúdo

---

## Próximas Ações Prioritárias

1. **Revogar Application Passwords expostas** - Segurança comprometida
2. **Gerar novas Application Passwords** - Atualizar 
3. **Limpar páginas duplicadas** - ofertasamazon tem 4 páginas WooCommerce duplicadas
4. **Ativar WooCommerce no ofertasamazon** - Plugin inativo apesar das páginas existirem
5. **Planejar conteúdo inicial** - Ambos os sites estão vazios
6. **Configurar Pretty Links** - Para operação de afiliados no ofertasamazon
7. **Atualizar título do trowinstore** - Ainda diz "Mude nas Configurações"

*Consulte docs/NEXT_ACTIONS.md para checklist completo*
