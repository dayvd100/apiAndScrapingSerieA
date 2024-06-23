import requests

# definindo a url da requisicao e os dados que vao ser passados
url_datas = "http://127.0.0.1:8000/datas/"
url_informations = "http://127.0.0.1:8000/informations/"
data = {"team_name": "Flamengo", "team_point": 50}

# pegando a resposta da requisicao
response_post_datas_team = requests.post(url_datas, json=data)

# verificando se os status code da requisicao foi ok
if response_post_datas_team.status_code == 200:
    print("Status code:", response_post_datas_team.status_code)
else:
    print("Erro")

# verificando se os status code da requisicao foi ok
response_get_datas_team = requests.get(url_informations)

if response_get_datas_team.status_code == 200:
    print(
        "Status code: ",
        response_get_datas_team.status_code,
    )
else:
    print("Erro2")
