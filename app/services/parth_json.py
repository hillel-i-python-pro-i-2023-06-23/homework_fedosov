import requests
import json



def read_file(link="http://api.open-notify.org/astros.json")->str:
    response = requests.get(link).text
    return response



def convert_json(file=read_file())->json:
    result = json.loads(file)
    return result

def save_astronauts(file=convert_json()):
    astronauts_number = file['number']
    astronauts = file['people']

    for astronaut in astronauts:
        name = astronaut['name']
        craft = astronaut['craft']
        yield name, craft

def show_astronauts(astronauts= save_astronauts()):
    astronauts_list = []
    for astronaut in astronauts:
        astronaut_str = ': '.join(astronaut)
        astronaut_reformat = f"<li><b>{astronaut_str}</b>"
        astronauts_list.append(astronaut_reformat)

    result = ''.join(astronauts_list)
    text = f'<b>In space we have 10 astronauts</b>'
    return f"{text}<br><ul>{result}</ul>"
