# Atlas Digital - Decisões Tomadas

## Prioridades do Projeto

| Prioridade | Status | Descrição |
|------------|--------|-----------|
| 1 | ✅ | Recuperar e estruturar trowinstore.com.br |
| 2 | ✅ | Estruturar ofertasamazon.trowinstore.com.br |
| 3 | ✅ | Criar operação de marketing de afiliados |
| 4 | ✅ | Automatizar tarefas repetitivas |
| 5 | ⏸️ | Evoluir AtlasBootstrap (somente depois) |

---

## Regras de Segurança

- ❌ NUNCA versionar credenciais, senhas ou tokens
- ❌ NUNCA expor secrets em qualquer formato
- ❌ NUNCA fazer deploy automático sem validação
- ✅ Usar arquivos `.example.json` como modelos públicos
- ✅ Manter configurações reais em arquivos locais ignorados pelo Git

### Padrões Ignorados pelo Git
```
**/config.local.json
**/config.secrets.json
**/.env
**/.env.*
config/*.local.json
config/secrets.json
config/secrets.local.json
wordpress/sites/*/config.local.json
wordpress/sites/*/.htaccess.local
automations/**/*.local.*
automations/**/credentials.json
wordpress/sites/**/wp-config.local.php
wordpress/sites/**/.htpasswd
```

---

## Decisões Arquiteturais

### 1. Repositório Monorepo
- Decisão: Manter todos os projetos em um único repositório
- Motivo: Simplicidade de gestão, versionamento único
- Data: 2026-07-26

### 2. Configuração Centralizada
- Decisão: Configurações públicas em `config/*.example.json`
- Motivo: Modelos versionáveis sem expor dados sensíveis
- Data: 2026-08-28

### 3. Automações Isoladas
- Decisão: WordPress em `automations/wordpress/`, afiliados em `automations/affiliate/`
- Motivo: Separação clara de responsabilidades
- Data: 2026-08-28

### 4. AtlasBootstrap como Ferramenta de Suporte
- Decisão: Congelar evolução do AtlasBootstrap temporariamente
- Motivo: Priorizar monetização e estruturação dos sites
- Data: 2026-08-28

---

## Padrões de Nomenclatura

- Arquivos de exemplo: `*.example.json`
- Arquivos locais: `*.local.json`
- Arquivos de segredos: `secrets.json`, `secrets.local.json`
- Scripts de automação: `*.ps1`, `*.sh`, `*.py`
