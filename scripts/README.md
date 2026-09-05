# Atlas Digital — Scripts

Scripts utilitários para automação e operações nos sites WordPress do projeto.

## atlas_exec.py

Executor unificado para ações comuns via REST API.

### Uso

```bash
python atlas_exec.py <acao> [site] [args]
```

### Ações disponíveis

| Ação | Descrição |
|------|-----------|
| `plugins` | Listar plugins ativos/inativos |
| `posts` | Listar posts publicados |
| `links` | Listar Pretty Links criados |
| `tagline` | Atualizar tagline do site |
| `css` | Injetar CSS customizado |

### Sites

- `trowinstore` — trowinstore.com.br
- `ofertasamazon` — ofertasamazon.trowinstore.com.br

### Exemplos

```bash
# Listar plugins do ofertasamazon
python scripts/atlas_exec.py plugins ofertasamazon

# Listar posts do trowinstore
python scripts/atlas_exec.py posts trowinstore

# Listar links de afiliado
python scripts/atlas_exec.py links ofertasamazon

# Atualizar tagline
python scripts/atlas_exec.py tagline trowinstore "Marketing de Afiliados"

# Injetar CSS customizado
python scripts/atlas_exec.py css ofertasamazon "body{background:#f5f5f5}"
```

## Requisitos

- Python 3.8+
- `config/sites.local.json` configurado (com Application Passwords válidas)
- Aplicar Passwords WordPress ativas em cada site
