from flask import (
    Flask,
    render_template,
)
from art import text2art

app = Flask(__name__)


def display_ascii_art(text):
    return text2art(text)


def get_info():
    full_name = 'David E. Bato-bato'
    course_name = 'Bachelor of Science in Computer Engineering'
    year = '1st year'
    section = '1-4'
    phrase = "Let's Go Software Development Team"
    return full_name, course_name, year, section, phrase
    


@app.route("/", methods=["GET", "POST"])
def index():
    full_name, course_name, year, section, phrase = get_info()
    ascii_art = display_ascii_art(f"GDSC-PUP")
    return render_template(
        "result.html",
        full_name=full_name,
        course_name=course_name,
        year=year,
        section=section,
        phrase=phrase,
        ascii_art=ascii_art,
    )


if __name__ == "__main__":
    app.run(debug=True)
