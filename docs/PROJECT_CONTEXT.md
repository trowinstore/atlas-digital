# Atlas Digital - Contexto do Projeto

## Visão Geral
O Atlas Digital é um projeto focado na criação e monetização de sites WordPress, com ênfase em marketing de afiliados e automação de tarefas repetitivas. O objetivo principal é gerar retorno financeiro através de sites de conteúdo e ofertas antes de investir em infraestrutura complexa.

## Arquitetura do Repositório

```
atlas-digital/
├── apps/
│   └── AtlasBootstrap/        # Bootstrap do ambiente PowerShell
├── config/                     # Configurações de sites e automações
│   ├── sites.example.json      # Sites WordPress (público)
│   └── automations.example.json # Configuração de automações (público)
├── wordpress/                  # Recursos relacionados a sites WordPress
│   ├── plugins/                # Plugins customizados
│   ├── snippets/               # Snippets de código WordPress
│   └── themes/                 # Temas customizados
├── automations/                # Scripts e ferramentas de automação
│   ├── wordpress/              # Automações para WordPress
│   └── affiliate/              # Automações para marketing de afiliados
├── scripts/                    # Scripts auxiliares diversos
├── tools/                      # Ferramentas externas/utilitárias
├── assets/                     # Ativos visuais e mídia
├── prompts/                    # Prompts para IA
├── core/                       # Núcleo reutilizável entre aplicações
├── docs/                       # Documentação do projeto
│   ├── specifications/         # Especificações técnicas
│   ├── PROJECT_CONTEXT.md      # Este arquivo
│   ├── CURRENT_STATUS.md       # Status atual do projeto
│   ├── DECISIONS.md            # Decisões arquiteturais
│   ├── NEXT_ACTIONS.md         # Próximas ações planejadas
│   └── AI_HANDOFF.md           # Instruções para continuidade com IA
└── README.md
```

## Princípios Fundamentais

1. **Retorno financeiro primeiro** — Priorizar ações que gerem receita ou validem o modelo de negócio antes de investir em complexidade técnica.
2. **Simplicidade operacional** — Evitar over-engineering. Cada componente deve ter um propósito claro e mensurável.
3. **Automação progressiva** — Automatizar apenas tarefas repetitivas já validadas manualmente.
4. **Versionamento seguro** — Nunca versionar credenciais, segredos ou dados sensíveis.
5. **Documentação viva** — Manter documentação atualizada com cada decisão relevante.

## Sites do Projeto

### Trowin Store
- **URL:** https://trowinstore.com.br
- **Propósito:** Site principal do projeto
- **Status:** Em estruturação
- **Plataforma:** WordPress

### Ofertas Amazon
- **URL:** https://ofertasamazon.trowinstore.com.br
- **Propósito:** Site de ofertas e marketing de afiliados
- **Status:** Em estruturação
- **Plataforma:** WordPress

## Convenções

- Toda configuração pública fica em `config/*.example.json`
- Configurações com credenciais ficam em `config/*.local.json` (ignorados pelo Git)
- Estrutura WordPress é versionada apenas em `wordpress/` (themes, plugins, snippets)
- Automações ficam isoladas em `automations/wordpress/` e `automations/affiliate/`
- Decisões importantes são registradas em `docs/DECISIONS.md`
- Status atualizado regularmente em `docs/CURRENT_STATUS.md`
