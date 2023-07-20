from flask import Flask
from app.services.users_generator import show_users
from app.services.file_reader import show_text
from app.services.parth_json import show_astronauts
from app.services.show_average import show_information


app = Flask(__name__)


@app.route('/get-content/')
def get_content():
    text = show_text()

    return text
@app.route('/generate-users/')
def show_users_list():
    users = show_users()

    return users

@app.route('/space/')
def space():
    astronauts = show_astronauts()

    return astronauts

@app.route('/mean/')
def mean():
    results = show_information()
    return results

if __name__ == '__main__':
    app.run(debug=True)