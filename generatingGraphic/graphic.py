import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import requests
import pandas as pd

response = requests.get("http://127.0.0.1:8000/informations/")
if response.status_code == 200:
    datas_json = response.json()
    dataframe_clubs = pd.DataFrame(datas_json)

    top_10_clubs = dataframe_clubs.head(10)

    top_10_clubs_sorted = top_10_clubs.sort_values(by="pontos", ascending=True)

    names = top_10_clubs_sorted["nome_time"]
    points = top_10_clubs_sorted["pontos"].astype(int)

    plt.figure(figsize=(12, 6))

    barras = plt.bar(names, points)
    plt.title("Gráfico de Barras - Pontuação dos Clubes")
    plt.xlabel("Nome do Clube")
    plt.ylabel("Pontos")

    plt.xticks(rotation=45, ha="right")

    # valores em cima da barra
    for barra in barras:
        altura = barra.get_height()
        plt.text(
            barra.get_x() + barra.get_width() / 2,
            altura,
            f"{altura}",
            ha="center",
            va="bottom",
        )

    plt.show()
else:
    print("Erro ao obter os dados. Código de status:", response.status_code)
