from flask import (
    Flask,
    render_template,
)
from art import text2art

app = Flask(__name__)


def display_ascii_art(text):
    return text2art(text)


def get_user_input():
    name = input("Enter name: ")
    age = input("Enter Age: ")
    address = input("Enter Address: ")
    age = int(age)
    return name, age, address


@app.route("/", methods=["GET", "POST"])
def index():
    name, age, address = get_user_input()
    ascii_art = display_ascii_art(f"Hello, {name.split()[0]}!")
    return render_template(
        "result.html", name=name, age=2023 - age, address=address, ascii_art=ascii_art
    )


if __name__ == "__main__":
    app.run(debug=True)
