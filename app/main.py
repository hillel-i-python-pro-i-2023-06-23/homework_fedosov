from app.services.file_reader import read_file

from app.services.parth_json import show_astronauts

from app.services.show_average import show_information

from app.services.users_generator import show_users

def main():
    print()
    text_file = 'some_text.txt'
    read_file(text_file)
    print()
    show_astronauts()
    print()
    show_information()
    print()
    show_users()

