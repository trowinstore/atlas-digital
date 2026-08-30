# Atlas Digital - Status Atual

## Estado do Repitório

**Branch atual:** main (origin/main sincronizado)

**Último commit:** 11694ab - "docs: atualizar CURRENT_STATUS com estado pós-commit 83589a4"

**Última verificação:** 2026-08-29

### Histórico de Commits Recentes
| Hash | Mensagem |
|------|----------|
| 11694ab | docs: atualizar CURRENT_STATUS com estado pós-commit 83589a4 |
| 83589a4 | feat: inicializar estrutura Atlas Digital |
| 6812888 | feat: implementa Workspace Launcher configurável |
| 5f2c19f | chore: adiciona logs ao gitignore |

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
- **Tema ativo:** standard-pro (não "Matrix")
- **WooCommerce:** Não instalado
- **Páginas (5):**
  - [35] Temos de Uso (terms-of-use)
  - [33] Politica de Privacidade (privacy-policy)
  - [31] Disclosure (disclosure)
  - [29] Contato (contact)
  - [25] Sobre Nos (about)
- **Posts:** 0 publicados
- **Categorias (2):** Videos (0 posts), What's New (0 posts)
- **Tags:** 0
- **Mídia (4):** bg1.jpg, post-banner.jpg, sidebar-banner.jpg, header-ad.jpg (2020/08)
- **Diagnóstico:** Site institucional abandonado, sem conteúdo real

### ofertasamazon.trowinstore.com.br
- **Status:** Ativo, API respondendo (HTTP 200, 5.1s)
- **Tema ativo:** astra (tema popular, leve, SEO-friendly)
- **WooCommerce:** ✅ Ativo
- **Páginas (11):**
  - [1008] Home
  - [1004] Contact
  - [1002] About
  - [1378-1381] Shop, Cart, Checkout, My Account (recentes)
  - [6-9] Shop, Cart, Checkout, My Account (antigas - duplicadas)
- **Posts:** 1 (Hello world! padrão)
- **Categorias (1):** Uncategorized (1 post)
- **Diagnóstico:** Loja WooCommerce vazia com páginas duplicadas

---

## Próximas Ações Prioritárias

1. **Configurar Application Passwords** - Para diagnóstico via API autenticada
2. **Limpar páginas duplicadas** - ofertasamazon tem 4 páginas WooCommerce duplicadas
3. **Planejar conteúdo** - Ambos os sites estão vazios
4. **Testar REST API autenticada** - Validar leitura/escrita
5. **Planejar automações** - Scripts para publicação

*Consulte docs/NEXT_ACTIONS.md para checklist completo*
