from app.file_reader import read_file
from app.parth_json import show_astronauts
from app.show_average import show_information
from app.users_generator import show_users

def run_homework():
    read_file()
    show_astronauts()
    show_information()
    show_users()

if __name__ == '__main__':
    run_homework()