# Atlas Digital - Próximas Ações

## Prioridade 1: Sites WordPress

### trowinstore.com.br
- [ ] Avaliar tema Matrix e planejar substituição
- [ ] Atualizar plugins pendentes (com backup prévio)
- [ ] Configurar tema customizado
- [ ] Revisar estrutura de categorias e posts
- [ ] Configurar SEO básico (All in One SEO)
- [ ] Configurar cache (LiteSpeed Cache)
- [ ] Ativar SSL (se não estiver)

### ofertasamazon.trowinstore.com.br
- [ ] Confirmar instalação separada do domínio principal
- [ ] Verificar tema atual
- [ ] Configurar links de afiliados (Pretty Links)
- [ ] Configurar categorias para ofertas
- [ ] Preparar plano de conteúdo inicial

---

## Prioridade 2: Automações WordPress

### Base
- [ ] Testar REST API em ambos os sites
- [ ] Listar posts, páginas, categorias via REST API
- [ ] Criar script de diagnóstico inicial
- [ ] Configurar Application Passwords (sem expor no Git)

### Publicação de Conteúdo
- [ ] Criar script para publicação de posts
- [ ] Configurar upload de mídia
- [ ] Preparar templates de posts de ofertas

---

## Prioridade 3: Automações de Afiliados

- [ ] Organizar links de afiliados (Pretty Links)
- [ ] Criar script de geração de posts de ofertas
- [ ] Configurar rastreamento de conversões
- [ ] Preparar base de dados de produtos

---

## Prioridade 4: Documentação e Operação

- [ ] Completar docs/DECISIONS.md
- [ ] Completar docs/AI_HANDOFF.md
- [ ] Criar docs/OPERATIONAL_GUIDE.md
- [ ] Configurar backup automatizado
- [ ] Configurar monitoramento de status

---

## Bloqueios Atuais

| Item | Motivo | Ação |
|------|--------|------|
| Atualização em massa de plugins | Risco de quebra | Fazer incrementalmente com rollback |
| Automação de publicação | API não testada | Testar REST API primeiro |
| Integração com Amazon Associates | Credenciais não configuradas | Configurar em arquivo .local |

---

## Pipeline de Trabalho Recomendado

```
VS Code → Git → GitHub → Atlas Digital → Automations → WordPress REST API → Sites
```

1. **Análise** — Entender estado atual dos sites
2. **Teste** — Validar REST API
3. **Automação** — Criar scripts de publicação
4. **Conteúdo** — Produzir posts de ofertas
5. **Monitoramento** — Acompanhar resultados
6. **Otimização** — Ajustar com base nos resultados
