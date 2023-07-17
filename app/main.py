from app.services.file_reader import read_file

from app.services.parth_json import show_astronauts

from app.services.show_average import show_information

from app.services.users_generator import show_users

def main():
    text_file = 'some_text.txt'
    read_file(text_file)
    show_astronauts()
    show_information()
    show_users()

if __name__ == '__main__':
    main()