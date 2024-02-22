#1. Mostrar os deputados de um determinado partido num estado. 
#   Ex.: deputados do PL em SP ou deputados do PT em MA
#2. Baixar as fotos dos deputados, dica: necessário fazer outro acesso à URL da foto com o requests

import requests

uf = 'ma'
partido= 'pt'

url = f'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaUf={uf}&siglaPartido={partido}'
dados = requests.get(url).json()
for dep in dados['dados']:
    with open('./imagens/' + dep['nome'] + '.jpg', 'wb') as file:
        req = requests.get(dep['urlFoto'], stream=True)
        if not req.ok:
            print("Ocorreu um erro, status:" , req.status_code)
        else:
            for dado in req.iter_content(1024):
                if not dado:
                    break

                file.write(dado)

        file.write(dado)



