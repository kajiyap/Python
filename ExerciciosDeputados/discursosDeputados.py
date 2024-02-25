#Analise os discursos de deputados. Por exemplo Deputada Tabata do Amaral. Novamente use um dicionário para guardar um contador das palavras, depois mostre em ordem decrescente da quantidade de palavras. Não se esqueça de tirar preposições, conjunções, etc. Uma boa forma de retirar Stop Words é usando a biblioteca NLTK.
#Cuidado: quando consumimos muitos dados de um endpoint, existe uma paginação, veja a lógica das páginas para poder pegar todos os dados. Está no final da saída mostrada no exemplo.


import requests
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords


ident = '204501'
dataInicio = '2023-05-20'
discursos = {}
pag = 1


url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{ident}/discursos?dataInicio={dataInicio}&ordenarPor=dataHoraInicio&ordem=ASC&pagina={pag}'
resposta = requests.get(url)

#CRIANDO O DICIONÁRIO puxando do json
while resposta.ok:
    
    dados = resposta.json()
    if len(dados['dados']) == 0:
        break
    
    for disc in dados['dados']:
        discursos[disc['dataHoraInicio']]=disc['transcricao']
        
    pag += 1
    url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{ident}/discursos?dataInicio={dataInicio}&ordenarPor=dataHoraInicio&ordem=ASC&pagina={pag}'
    resposta = requests.get(url)


#removendo preposições, conjunções e etc
for k, v in discursos.items():
    palavras = nltk.word_tokenize(v)
    stop_words = set(stopwords.words('portuguese'))
    palavras_filtradas = [palavra for palavra in palavras if palavra.lower() not in stop_words]
#atribuindo a quantidade de palavras a uma chave
    discursos[k] = len(palavras_filtradas)
    

dicionarioOrdem = dict(sorted(discursos.items(), key=lambda item: item[1], reverse=True))
for x, y in dicionarioOrdem.items():
    print (x, y)
    
    

    
