from selenium import webdriver
from selenium.webdriver.common.by import By
import json

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

        json_data = json.dumps(teams_points_and_names, ensure_ascii=False)

        return json_data

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return {"error": str(e)}

    finally:
        browser.quit()


if __name__ == "__main__":
    json_data = getting_data_and_transforming_in_json()
    parsed_data = json.loads(json_data)
    print(parsed_data)
