#Mostrar os fornecedores em ordem do valor que mais receberam da cota parlamentar, em ordem decrescente, use um dicionário para guardar todos os valores
#Dica: lembre que existe o sorted(dicionário, key=função, ...) onde a função irá devolver o valor para um determinado item do dicionário.
#   Ex.: Mostrar os maiores fornecedores que receberam verbas da deputada Tabata do Amaral em 2023

import requests

ident = '204501'
ano= '2023'
pag = 1

fornecedores = {}
    

url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{ident}/despesas?ano={ano}&ordem=ASC&ordenarPor=ano&pagina={pag}&itens=15'
resposta = requests.get(url)
while resposta.ok:
    dados = resposta.json()
    if len(dados['dados']) == 0:
        break
    
    for forn in dados['dados']:
        if fornecedores.get(forn['nomeFornecedor']) == None:
            fornecedores[forn['nomeFornecedor']] = forn['valorLiquido']
        else:
            fornecedores[forn['nomeFornecedor']] += forn['valorLiquido']
    
    pag += 1
    url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{ident}/despesas?ano={ano}&ordem=ASC&ordenarPor=ano&pagina={pag}&itens=15'
    resposta = requests.get(url)

for k, v in fornecedores.items():
    print(k, v)