"""
Script para atualizar páginas PT-BR no trowinstore.com.br
"""
import json
import urllib.request
import urllib.error
import base64
from pathlib import Path

CONFIG = Path('config/sites.local.json')


def load_config():
    with open(CONFIG, encoding='utf-8') as f:
        return json.load(f)


def auth(site):
    return base64.b64encode(
        (site['username'] + ':' + site['application_password']).encode()
    ).decode()


def update_page(site, page_id, title, content):
    url = site['url'] + '/wp-json/wp/v2/pages/' + str(page_id)
    headers = {
        'Authorization': 'Basic ' + auth(site),
        'Content-Type': 'application/json'
    }
    data = json.dumps({'title': title, 'content': content}).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return True, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return False, e.read().decode()[:200]


def main():
    c = load_config()
    site = c['sites']['trowinstore']

    # Conteudos das paginas
    contact = '''<div style="max-width:600px;margin:0 auto;">
<h2 style="color:#1A2238;text-align:center;margin-bottom:20px;">Entre em Contato</h2>
<p style="text-align:center;color:#555;margin-bottom:30px;">Tem duvidas, sugestoes ou propostas de parceria? Preencha o formulario abaixo!</p>
<form action="#" method="post" style="background:#f9f9f9;padding:30px;border-radius:12px;border:1px solid #e0e0e0;">
<div style="margin-bottom:20px;"><label style="display:block;font-weight:600;color:#333;margin-bottom:8px;">Nome:</label><input type="text" name="nome" required style="width:100%;padding:12px;border:1px solid #ccc;border-radius:8px;" placeholder="Seu nome"></div>
<div style="margin-bottom:20px;"><label style="display:block;font-weight:600;color:#333;margin-bottom:8px;">Email:</label><input type="email" name="email" required style="width:100%;padding:12px;border:1px solid #ccc;border-radius:8px;" placeholder="seu@email.com"></div>
<div style="margin-bottom:20px;"><label style="display:block;font-weight:600;color:#333;margin-bottom:8px;">Assunto:</label><select name="assunto" required style="width:100%;padding:12px;border:1px solid #ccc;border-radius:8px;background:#fff;"><option value="">Selecione um assunto</option><option value="duvida">Duvida Geral</option><option value="parceria">Proposta de Parceria</option><option value="afiliado">Programa de Afiliado</option><option value="sugestao">Sugestao de Conteudo</option><option value="outro">Outro Assunto</option></select></div>
<div style="margin-bottom:20px;"><label style="display:block;font-weight:600;color:#333;margin-bottom:8px;">Mensagem:</label><textarea name="mensagem" rows="5" required style="width:100%;padding:12px;border:1px solid #ccc;border-radius:8px;resize:vertical;" placeholder="Escreva sua mensagem"></textarea></div>
<div style="text-align:center;"><button type="submit" style="background:linear-gradient(135deg,#00E5FF 0%,#B026FF 100%);color:#1A2238;border:none;padding:15px 40px;border-radius:8px;font-weight:700;text-transform:uppercase;cursor:pointer;">Enviar Mensagem</button></div>
</form>
<div style="margin-top:40px;text-align:center;background:#1A2238;color:#fff;padding:25px;border-radius:12px;">
<h3 style="margin-bottom:15px;color:#00E5FF;">Outros Canais</h3>
<p style="margin-bottom:10px;"><strong>Email:</strong> <a href="mailto:suporte@trowinstore.com.br" style="color:#00E5FF;">suporte@trowinstore.com.br</a></p>
<p style="margin-bottom:0;color:rgba(255,255,255,0.8);font-size:14px;">Respondemos em ate 48 horas uteis.</p>
</div>
</div>'''

    termos = '''<h2>Termos de Uso</h2>
<p><em>Ultima atualizacao: 06 de setembro de 2026</em></p>
<h3>1. Aceitacao dos Termos</h3>
<p>Ao acessar e utilizar o site <strong>TROWIN STORE</strong>, voce reconhece ter lido, compreendido e concordado com os presentes Termos de Uso.</p>
<h3>2. Descricao do Servico</h3>
<p>A <strong>TROWIN STORE</strong> e uma plataforma digital que oferece conteudo informativo sobre marketing de afiliados, tutoriais de YouTube e estrategias de empreendedorismo digital.</p>
<h3>3. Links de Afiliado</h3>
<p>O site pode conter links para produtos ou servicos de terceiros. <strong>TROWIN STORE</strong> pode receber uma comissao por compras realizadas atraves desses links, sem nenhum custo adicional para voce.</p>
<p><strong>Importante:</strong> Os precos e disponibilidade dos produtos podem variar. Nao nos responsabilizamos por transacoes realizadas em sites de terceiros.</p>
<h3>4. Propriedade Intelectual</h3>
<p>Todo o conteudo publicado no site e protegido por leis de direitos autorais. E proibida a reproducao, distribuicao ou modificacao sem autorizacao previa.</p>
<h3>5. Isencao de Responsabilidade</h3>
<p>As informacoes presentes no site sao fornecidas apenas para fins informativos. <strong>TROWIN STORE</strong> nao garante resultados especificos com as estrategias, produtos ou servicos mencionados.</p>
<h3>6. Privacidade</h3>
<p>Respeitamos sua privacidade. Para mais detalhes, consulte nossa <a href="/politica-de-privacidade/">Politica de Privacidade</a>.</p>
<h3>7. Modificacoes nos Termos</h3>
<p>Reservamos o direito de modificar estes termos a qualquer momento.</p>
<h3>8. Lei Aplicavel</h3>
<p>Estes Termos de Uso sao regidos pelas leis brasileiras.</p>
<h3>9. Contato</h3>
<p>Para duvidas, entre em contato atraves da nossa pagina de <a href="/contato/">Contato</a> ou pelo email: <a href="mailto:suporte@trowinstore.com.br">suporte@trowinstore.com.br</a></p>'''

    privacidade = '''<h2>Politica de Privacidade</h2>
<p><em>Ultima atualizacao: 06 de setembro de 2026</em></p>
<h3>1. Introducao</h3>
<p>A <strong>TROWIN STORE</strong> esta comprometida com a protecao da sua privacidade.</p>
<h3>2. Informacoes que Coletamos</h3>
<h4>2.1 Dados de Navegacao</h4>
<p>Quando voce acessa nosso site, podemos coletar:</p>
<ul>
<li>Endereco IP</li>
<li>Tipo de navegador e versao</li>
<li>Sistema operacional</li>
<li>Paginas visitadas e tempo de permanencia</li>
<li>Data e hora do acesso</li>
</ul>
<h4>2.2 Cookies</h4>
<p>Utilizamos cookies para:</p>
<ul>
<li>Melhorar a experiencia do usuario</li>
<li>Analisar o trafego do site (Google Analytics)</li>
<li>Lembrar suas preferencias</li>
<li>Exibir anuncios personalizados</li>
</ul>
<h4>2.3 Dados Voluntarios</h4>
<p>Caso voce preencha nosso formulario de contato, coletaremos: nome, email, assunto e mensagem.</p>
<h3>3. Uso das Informacoes</h3>
<p>Utilizamos suas informacoes para:</p>
<ul>
<li>Responder suas mensagens e pedidos de contato</li>
<li>Melhorar nosso site e conteudo</li>
<li>Analisar metricas de acesso</li>
<li>Enviar comunicacoes (apenas se voce solicitar)</li>
<li>Exibir anuncios relevantes</li>
</ul>
<h3>4. Compartilhamento de Dados</h3>
<p><strong>Nao vendemos</strong> suas informacoes pessoais. Podemos compartilhar dados com:</p>
<ul>
<li>Google Analytics para analise de trafego</li>
<li>Servicos de email para envio de respostas</li>
<li>Autoridades legais quando exigido por lei</li>
</ul>
<h3>5. Seus Direitos (LGPD)</h3>
<p>De acordo com a Lei Geral de Protecao de Dados (LGPD - Lei 13.709/2018), voce tem direito a:</p>
<ul>
<li>Confirmar a existencia de tratamento de dados</li>
<li>Acessar seus dados pessoais</li>
<li>Corrigir dados incompletos ou desatualizados</li>
<li>Solicitar a anonimizacao ou exclusao de dados</li>
<li>Solicitar a portabilidade dos dados</li>
<li>Revogar consentimento a qualquer momento</li>
</ul>
<h3>6. Seguranca dos Dados</h3>
<p>Implementamos medidas de seguranca tecnicas e administrativas para proteger suas informacoes contra acesso nao autorizado, alteracao ou destruicao.</p>
<h3>7. Links Externos</h3>
<p>Nosso site pode conter links para sites de terceiros. Nao nos responsabilizamos pelas praticas de privacidade desses sites.</p>
<h3>8. Alteracoes nesta Politica</h3>
<p>Esta Politica de Privacidade pode ser atualizada periodicamente. Recomendamos que voce revise esta pagina regularmente.</p>
<h3>9. Contato</h3>
<p>Para exercitar seus direitos ou esclarecer duvidas, entre em contato:</p>
<ul>
<li>Email: <a href="mailto:suporte@trowinstore.com.br">suporte@trowinstore.com.br</a></li>
<li>Formulario: <a href="/contato/">Pagina de Contato</a></li>
</ul>'''

    # Atualizar paginas
    print("=" * 70)
    print("ATUALIZACAO DE PAGINAS PT-BR - TROWIN STORE")
    print("=" * 70)

    for page_id, title, content in [
        (29, 'Contato', contact),
        (351, 'Termos de Uso', termos),
        (350, 'Politica de Privacidade', privacidade),
    ]:
        ok, result = update_page(site, page_id, title, content)
        status = '[OK]' if ok else '[ERRO]'
        print(f"\n{status} Pagina {title} (ID {page_id})")
        if not ok:
            print(f"  Erro: {result}")

    print("\n" + "=" * 70)
    print("AJUSTES CONCLUIDOS!")
    print("=" * 70)


if __name__ == '__main__':
    main()
