from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://ge.globo.com/futebol/brasileirao-serie-a/"


def getting_data_and_transforming_in_json():
    try:
        browser = webdriver.Chrome()
        browser.get(url)

        team_names = browser.find_elements(By.XPATH, "//tbody//tr//strong")
        points = browser.find_elements(
            By.XPATH,
            "//td[@class='classificacao__pontos classificacao__pontos--ponto']",
        )

        teams_points_and_names = []

        for team_name, point in zip(team_names, points):
            team_data = {"nome_time": team_name.text, "pontos": point.text}
            teams_points_and_names.append(team_data)

        return teams_points_and_names

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return {"error": str(e)}

    finally:
        browser.quit()
