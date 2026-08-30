# Atlas Digital - Status Atual

## Estado do Repositório

**Branch atual:** main (origin/main sincronizado)

**Último commit:** 83589a4 - "feat: inicializar estrutura Atlas Digital"

**Última verificação:** 2026-08-29

### Histórico de Commits Recentes
| Hash | Mensagem |
|------|----------|
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

## Estado dos Sites

### trowinstore.com.br
- **Status:** Ativo (recuperado do modo manutenção)
- **Tema:** Template "Matrix" (antigo/cru)
- **Conteúdo identificado:**
  - Páginas: Home, Sobre Nós, Contato, Disclosure, Política de Privacidade, Termos de Uso
  - Categorias: "Quais as Novidades", "Videos"
  - Mensagens padrão: "Nothing found"
  - Referências antigas: "Mude nas Configurações", "Tagline"

### ofertasamazon.trowinstore.com.br
- **Status:** Modo manutenção desativado
- **Situação:** Houve confusão anterior com instalação do domínio principal
- **Próximo passo:** Confirmar separação clara das instalações

---

## Próximas Ações Prioritárias

1. **Diagnosticar trowinstore.com.br** - Tema, plugins, conteúdo
2. **Diagnosticar ofertasamazon.trowinstore.com.br** - Instalação, tema, plugins
3. **Testar REST API** - Validar acesso não-invasivo aos sites
4. **Planejar automações** - Scripts para publicação de conteúdo

*Consulte docs/NEXT_ACTIONS.md para checklist completo*
