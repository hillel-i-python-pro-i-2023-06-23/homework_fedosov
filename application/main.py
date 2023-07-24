from application.services.file_reader import read_file

from application.services.parth_json import show_astronauts

from application.services.show_average import show_information

from application.services.users_generator import show_users

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

