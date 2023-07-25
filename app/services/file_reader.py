from app.config import FILES_INPUT_DIR

def read_file(file_name)->str:
    PATH = FILES_INPUT_DIR.joinpath(file_name)
    with open(PATH, 'r') as file:
        result = file.read()
    print('EX #1')
    print(result)

