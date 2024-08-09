'''
1- Abrir o navegador [x]
2- Verificar se o navegador foi aberto
3- Digitar a Url
4- Digitar email
5- Clicar em continuar ou apertar enter
6- Selecionar campo senha
7- Digitar a senha
8- Clicar em entrar ou apertar enter
9- Clicar no botão acessar
10- Clicar no botão "depois" do alerta que vai aparecer
11- Clicar no botão finanças
12- Colocar o mouse em cima da aba finanças
13- Localizar "Contas a Receber"
14- Clicar em "exibir todas" abaixo de contar a receber
15- Localizar o icone do filtro ou o nome da coluna "Número do Documento"
16- Clicar no campo do filtro
17- Digitar o contrato
18- Pressionar 'Enter'
19- Clicar na coluna de parcelas para reordenar da maior para a menor
20- localizar todos os checkbox
21- Criar um loop para dar dois clicks ao lado de cada checkbox para entrar no contrato
22- Selecionar Diversos
23- Localizar a label "Número de Parcela"
24- Dar um click na label
25- Pegar input da parcela
26- Formatar input
27- Comparar input com parcela do extrato

28.True- Se os dados forem iguais vai clicar no Recebimentos
29.True- Clicar em Registrar Recebimento
30.True- Selecionar a label 'Data de Recebimento'
31.True- Colar a data do informada no sistema
32.True- Clicar en "Confirmar Recebimento"

28.False- Se os dados forem diferentes vai clicar em voltar
29.False- O loop vai pular para o próximo contrato
30.False- Se o contrato não for encontrado pula para o próximo do array


'''

from AutomationWeb import AutomationWeb
from env import url, titulo, login, senha
import time

browser = AutomationWeb(tempo_de_espera=20)
browser.abrir_navegador(url)
browser.pegar_titulo_navegador(titulo)

# Seleciona o campo e-mail e digitar o email
browser.encontrar_elemento_name('email')
browser.digitar(login)

# Click no botão continue
browser.encontrar_elemento_id('btn-continue')
browser.clicar_elemento()

# Seleciona o campo senha e digita a senha
browser.encontrar_elemento_id('current-password')
browser.digitar(senha)

# Click no botão entrar
browser.encontrar_elemento_id('btn-login')
browser.clicar_elemento()

# Clica em botão acessar
browser.encontrar_elemento_xpath('//*[@id="root"]/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div/button')
browser.clicar_elemento()

# Troca de janela para a segunda aba
browser.trocar_janela()

# Encontra e clica no botão financeiro
browser.encontrar_elemento_xpath('//*[@id="tiles"]/li[5]/a')
browser.clicar_elemento()

tempo = 0
while tempo < 10:
    time.sleep(1)
    print(tempo)
    tempo += 1

# Fechando alerta
browser.encontrar_elemento_id('onesignal-slidedown-cancel-button')
browser.clicar_elemento()

# Clica na aba financeiro
browser.encontrar_elemento_xpath('//*[@id="app"]/header/div[3]/div/ul/li[5]/a')
browser.clicar_elemento()

tempo = 0
while tempo < 10:
    time.sleep(1)
    print(tempo)
    tempo += 1

# Clicando na categoria exibir todas
browser.encontrar_elemento_xpath('//*[@id="d0cundefined"]/div/div[2]/div[3]/ul/li[3]/a')
browser.clicar_elemento()

browser.fechar_navegador()