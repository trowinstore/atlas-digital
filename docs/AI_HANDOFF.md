# Atlas Digital - AI Handoff

## Instruções para Continuidade com IA

Este arquivo define o protocolo para que qualquer IA (Claude, GPT, etc.) atue no projeto Atlas Digital de forma segura e consistente.

---

## Fluxo Obrigatório

Antes de qualquer alteração de arquivos, seguir este fluxo:

1. **Analisar** — Entender o estado atual do repositório
2. **Planejar** — Listar as alterações propostas
3. **Explicar** — Justificar cada alteração
4. **Aguardar** — Confirmação explícita do usuário
5. **Executar** — Realizar as alterações
6. **Mostrar** — git diff para revisão
7. **Não Commitar** — Aguardar aprovação para commit

---

## Regras de Ouro

### ❌ Nunca Fazer
- ❌ Fazer commit sem aprovação explícita
- ❌ Modificar o AtlasBootstrap sem necessidade direta
- ❌ Versionar credenciais, senhas, tokens ou segredos
- ❌ Executar deploy automático sem validação
- ❌ Atualizar plugins WordPress em massa sem backup
- ❌ Criar abstrações prematuras
- ❌ Modificar sistemas em funcionamento sem necessidade

### ✅ Sempre Fazer
- ✅ Ler este arquivo antes de qualquer tarefa
- ✅ Verificar `git status` antes de alterar
- ✅ Usar arquivos `.example.json` como modelos
- ✅ Manter configurações reais em arquivos locais
- ✅ Explicar motivo de cada alteração
- ✅ Mostrar diff antes de commitar

---

## Prioridade Atual

O foco principal é:

1. **Recuperar e estruturar trowinstore.com.br**
2. **Estruturar ofertasamazon.trowinstore.com.br**
3. **Criar automações simples para operação dos sites**
4. **Evoluir posteriormente automação de conteúdo e marketing de afiliados**

O AtlasBootstrap permanece **congelado** como ferramenta de suporte.

---

## Estrutura de Referência

```
atlas-digital/
├── apps/AtlasBootstrap/        # Congelado
├── config/                     # Configurações públicas
│   ├── sites.example.json      # Sites WordPress
│   └── automations.example.json # Automações
├── wordpress/                  # Recursos WordPress
│   ├── plugins/
│   ├── snippets/
│   └── themes/
├── automations/                # Scripts de automação
│   ├── wordpress/
│   └── affiliate/
├── scripts/                    # Scripts auxiliares
├── assets/                     # Ativos visuais
├── prompts/                    # Prompts para IA
├── docs/                       # Documentação
│   ├── PROJECT_CONTEXT.md      # Contexto completo
│   ├── CURRENT_STATUS.md       # Status atual
│   ├── DECISIONS.md            # Decisões tomadas
│   ├── NEXT_ACTIONS.md         # Próximas ações
│   └── AI_HANDOFF.md           # Este arquivo
└── README.md
```

---

## Configuração de Sites

### Trowin Store
- URL: https://trowinstore.com.br
- REST API: https://trowinstore.com.br/wp-json/wp/v2

### Ofertas Amazon
- URL: https://ofertasamazon.trowinstore.com.br
- REST API: https://ofertasamazon.trowinstore.com.br/wp-json/wp/v2

---

## Comandos Úteis

```bash
# Verificar estado do repositório
git -C K:/Projetos/atlas-digital status

# Ver diff de um arquivo específico
git -C K:/Projetos/atlas-digital diff -- <arquivo>

# Listar estrutura de diretórios
find K:/Projetos/atlas-digital/<diretorio> -type f -o -type d | sort
```

---

## Segurança

Nunca versionar:
- Credenciais WordPress
- Senhas de banco de dados
- Application Passwords
- Tokens
- API Keys
- Secrets

Usar arquivos locais ignorados pelo Git.
