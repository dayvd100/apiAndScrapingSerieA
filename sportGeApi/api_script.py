from fastapi import FastAPI
from sportGeScraping.scraping_script import getting_data_and_transforming_in_json

app = FastAPI()


@app.get("/informations/")
def execute_the_get_function_informations():
    try:
        return getting_data_and_transforming_in_json()
    except Exception as e:
        return {"error": str(e)}
