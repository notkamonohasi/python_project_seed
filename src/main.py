from src.optimize import optimize
from src.type import ApiInput, ApiOutput


def main(api_input: ApiInput) -> ApiOutput:
    print(f"{api_input=}")
    return optimize(api_input)
