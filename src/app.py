from main import main
from type import ApiInput


def lambda_handler(body: dict):
    api_input = ApiInput(**body)
    return main(api_input)
