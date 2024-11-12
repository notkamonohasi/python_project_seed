from fastapi import FastAPI

from src.main import main
from src.type import ApiInput

app = FastAPI(debug=True)


@app.get("/id")
def _id(api_input: ApiInput):
    """
    dummy function
    """
    return main(api_input)


@app.get("/solve")
def _solve(api_input: ApiInput):
    """
    dummy function
    """
    return main(api_input)
