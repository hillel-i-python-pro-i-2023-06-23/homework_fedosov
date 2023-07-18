from app.config import FILES_INPUT_DIR

def read_file(file_name=FILES_INPUT_DIR.joinpath('some_text.txt')):
    PATH = file_name
    with open(PATH, 'r') as file:
        result = file.read()
    return result

def show_text(text=read_file()):
    return text