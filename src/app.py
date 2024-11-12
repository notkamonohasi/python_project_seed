from src.main import main
from src.type import ApiInput


def lambda_handler(body: dict):
    api_input = ApiInput(**body)
    return main(api_input)
