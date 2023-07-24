from flask import Flask, Response
from webargs import fields
from webargs.flaskparser import use_args

from application.services.create_table import create_table
from application.services.db_connection import DBConnection
from application.services.users_generator import show_users
from application.services.file_reader import show_text
from application.services.parth_json import show_astronauts
from application.services.show_average import show_information


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


@app.route("/phones/create")
@use_args({'contact_name': fields.Str(required=True), "phone_value": fields.Int(required=True)}, location="query")
def users__create(args):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "INSERT INTO phones (contact_name, phone_value) VALUES (:contact_name, :phone_value);",
                {"contact_name": args['contact_name'], "phone_value": args['phone_value']},
            )

    return "Ok"


@app.route("/phones/read-all")
def users__read_all():
    with DBConnection() as connection:
        contacts = connection.execute("SELECT * FROM phones;").fetchall()

    return "<br>".join([f'{contact["pk"]}: {contact["contact_name"]} - {contact["phone_value"]}' for contact in contacts])


@app.route("/phones/read/<int:pk>")
def users__read(pk: int):
    with DBConnection() as connection:
        contact = connection.execute(
            "SELECT * " "FROM phones " "WHERE (pk=:pk);",
            {
                "pk": pk,
            },
        ).fetchone()

    return f'{contact["pk"]}: {contact["contact_name"]} - {contact["phone_value"]}'


@app.route("/phones/update/<int:pk>")
@use_args({"name": fields.Str(), "number": fields.Int()}, location="query")
def users__update(
    args,
    pk: int,
):
    with DBConnection() as connection:
        with connection:
            name = args.get("contact_name")
            number = args.get("phone_value")
            if name is None or number is None:
                return Response(
                    "Need to provide at least one argument",
                    status=400,
                )

            args_for_request = []
            if name is not None:
                args_for_request.append("contact_name=:name")
            if number is not None:
                args_for_request.append("phone_value=:number")

            args_2 = ", ".join(args_for_request)

            connection.execute(
                "UPDATE phones " f"SET {args_2} " "WHERE pk=:pk;",
                {
                    "pk": pk,
                    "phone_value": number,
                    "contact_name": name,
                },
            )

    return "Ok"


@app.route("/phones/delete/<int:pk>")
def users__delete(pk):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "DELETE " "FROM phones " "WHERE (pk=:pk);",
                {
                    "pk": pk,
                },
            )

    return "Ok"



create_table()

if __name__ == '__main__':
    app.run(debug=True,port=8000)