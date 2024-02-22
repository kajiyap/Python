#Analise os discursos de deputados. Por exemplo Deputada Tabata do Amaral. Novamente use um dicionário para guardar um contador das palavras, depois mostre em ordem decrescente da quantidade de palavras. Não se esqueça de tirar preposições, conjunções, etc. Uma boa forma de retirar Stop Words é usando a biblioteca NLTK.
#Cuidado: quando consumimos muitos dados de um endpoint, existe uma paginação, veja a lógica das páginas para poder pegar todos os dados. Está no final da saída mostrada no exemplo.
import requests

ident = '204501'
dataInicio = '2023-05-20'
discursos = {}
pag = 1


url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{ident}/discursos?dataInicio={dataInicio}&ordenarPor=dataHoraInicio&ordem=ASC'
resposta = requests.get(url)
while resposta.ok:
    dados = resposta.json()
    if len(dados['dados']) == 0:
        break
    
    for disc in dados['dados']:
        disc = disc['transcricao']
        print (disc)
    
    pag += 1
    url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{ident}/discursos?dataInicio={dataInicio}&ordenarPor=dataHoraInicio&ordem=ASC'
    resposta = requests.get(url)

for k, v in discursos.items():
    print(k, v)
