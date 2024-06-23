from fastapi import FastAPI
from models.models import Datas

app = FastAPI()

datas = Datas

team_information = []


# Criando a rota e dando uma funcao para o metodo post
@app.post("/datas/")
async def create_datas(datas: Datas):
    print(datas.team_name, datas.team_point)
    team_information.append({datas.team_name, datas.team_point})
    return {
        "Nome do time": datas.team_name,
        "Pontos do time": datas.team_point,
    }


# Criando a rota e dando uma funcao para o metodo get
@app.get("/informations/")
async def get_information():
    return team_information
