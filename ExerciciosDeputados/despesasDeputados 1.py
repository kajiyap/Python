#Calcular o total gasto com a cota parlamentar de um determinado deputado, num determinado ano.
#   Ex.: Valor líquido dos gastos da Deputada Tabata do Amaral em 2023

import requests

ident = '204501'
ano= '2023'
pag = 1
gastoTotal = 0

url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{ident}/despesas?ano={ano}&ordem=ASC&ordenarPor=ano&pagina={pag}&itens=15'
resposta = requests.get(url)
while resposta.ok:
    dados = resposta.json()
    if len(dados['dados']) == 0:
        break
    for gastos in dados['dados']:
        gastoTotal = gastoTotal + gastos['valorLiquido']
    pag += 1

    url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{ident}/despesas?ano={ano}&ordem=ASC&ordenarPor=ano&pagina={pag}&itens=15'
    resposta = requests.get(url)

print(gastoTotal)
