# Atlas Digital — Scripts

Scripts utilitários para automação e operações nos sites WordPress do projeto.

## atlas_exec.py (v2.0)

Executor unificado para ações via REST API.

### Uso

```bash
python atlas_exec.py <acao> [site] [args...]
```

### Alias PowerShell (recomendado)

```powershell
function atlas { python K:/Projetos/atlas-digital/scripts/atlas_exec.py @args }
Set-Alias -Name atlas -Value atlas
```

### Ações disponíveis (13 ações)

#### Listagem
| Ação | Descrição |
|------|-----------|
| `plugins` | Listar plugins ativos/inativos |
| `posts` | Listar posts publicados |
| `pages` | Listar paginas |
| `links` | Listar Pretty Links |
| `categories` | Listar categorias |
| `diagnostic` | Diagnostico completo do site |

#### Criação
| Ação | Descrição |
|------|-----------|
| `create-post` | Criar novo post |
| `create-link` | Criar Pretty Link |

#### Atualização
| Ação | Descrição |
|------|-----------|
| `update-post` | Atualizar post existente |
| `tagline` | Atualizar tagline do site |
| `css` | Injetar CSS customizado |

#### Exclusão
| Ação | Descrição |
|------|-----------|
| `delete-post` | Mover/excluir post (com flag `--force`) |
| `delete-link` | Excluir Pretty Link (com flag `--force`) |

### Sites

- `trowinstore` — trowinstore.com.br
- `ofertasamazon` — ofertasamazon.trowinstore.com.br

### Exemplos

```powershell
# Listagens
atlas plugins ofertasamazon
atlas posts trowinstore
atlas pages trowinstore
atlas links ofertasamazon
atlas categories ofertasamazon
atlas diagnostic ofertasamazon

# Criar
atlas create-post trowinstore "Meu Post" "Conteudo do post aqui"
atlas create-link ofertasamazon "Cadeira Gamer" "https://amazon.com/dp/B08N5WRWNW"

# Atualizar
atlas update-post trowinstore 314 "Novo Titulo" "Novo conteudo" "publish"
atlas tagline trowinstore "Marketing de Afiliados"
atlas css trowinstore "body{font-family:Segoe UI}"

# Excluir (com confirmacao)
atlas delete-post trowinstore 313        # Apenas verifica
atlas delete-post trowinstore 313 --force # Move para lixeira
```

## Requisitos

- Python 3.8+
- `config/sites.local.json` configurado (com Application Passwords válidas)
- Application Passwords WordPress ativas em cada site
- Plugin WPCode ativo (para a ação `css`)

## Configuração

Edite `config/sites.local.json`:

```json
{
  "description": "Credenciais locais dos sites. NUNCA commit este arquivo!",
  "version": "1.0.0",
  "sites": {
    "trowinstore": {
      "url": "https://trowinstore.com.br",
      "username": "atlas-api",
      "application_password": "SUA_SENHA_AQUI"
    },
    "ofertasamazon": {
      "url": "https://ofertasamazon.trowinstore.com.br",
      "username": "atlas-api",
      "application_password": "SUA_SENHA_AQUI"
    }
  }
}
```

## Segurança

- O arquivo `config/sites.local.json` está no `.gitignore`
- NUNCA commite credenciais reais
- A flag `--force` é necessária para ações destrutivas (exclusão)
- A ação `delete-post` move o post para a lixeira por padrão (não exclui permanentemente)
