import requests
import json
from typing import Any


def read_file(link="http://api.open-notify.org/astros.json") -> str:
    response = requests.get(link).text
    return response


def convert_json(file: str = None) -> dict[str, Any]:
    if file is None:
        file = read_file()
    result = json.loads(file)
    return result


def show_astronauts(file=None):
    if file is None:
        file = convert_json()
    astronauts_number = file["number"]
    astronauts = file["people"]
    print("Ex #2")
    print(f"We have {astronauts_number} astronauts:\n")
    for astronaut in astronauts:
        name = astronaut["name"]
        craft = astronaut["craft"]
        print(f"Name: {name}\nCraft: {craft}\n")
