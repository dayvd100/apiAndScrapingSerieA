from fastapi import FastAPI
from sportGeScraping.scraping_script import getting_data_and_transforming_in_json

app = FastAPI()


@app.get("/informations/")
def execute_the_get_function_informations():
    try:
        return getting_data_and_transforming_in_json()
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
