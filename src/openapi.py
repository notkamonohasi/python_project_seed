from fastapi import FastAPI

from optimize import optimize
from type import ApiInput, ApiOutput

app = FastAPI(debug=True)


@app.post("/auth")
def _auth(api_input: ApiInput) -> bool:
    """
    dummy function
    """
    return api_input.id == "kamonohasi"


@app.post("/optimize")
def _optimize(api_input: ApiInput) -> ApiOutput:
    """
    dummy function
    """
    return optimize(api_input)


if __name__ == "__main__":
    import json

    with open("swagger.json", "w") as f:
        json.dump(app.openapi(), f, indent=4)
