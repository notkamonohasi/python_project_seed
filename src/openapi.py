from fastapi import FastAPI

from optimize import optimize
from type import ApiInput

app = FastAPI(debug=True)


@app.get("/auth")
def _auth(api_input: ApiInput):
    """
    dummy function
    """
    return api_input.id == "kamonohasi"


@app.get("/optimize")
def _optimize(api_input: ApiInput):
    """
    dummy function
    """
    return optimize(api_input)
