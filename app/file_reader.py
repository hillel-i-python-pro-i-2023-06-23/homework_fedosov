from app.config import FILES_INPUT_DIR

def read_file(PATH=FILES_INPUT_DIR.joinpath('some_text.txt'))->str:

    with open(PATH, 'r') as file:
        result = file.read()

    return "\n" + result


def show_text(text=read_file())->str:
    print('Ex #1')
    print(text)

show_text()