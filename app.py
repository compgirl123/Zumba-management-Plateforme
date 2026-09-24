from flask import Flask, request, render_template

app = Flask(__name__)

options = [
    "View participants",
    "View details",
    "View participant details",
    "add participant",
    "remove participant",
    "remove participants without subscription",
    "number of participants in each level",
    "participants for each dance type",
    "participants for a specific dance type"
]

levels = [
    "beginner",
    "intermediaire",
    "advanced"
]

danceTypes = [
    "bachata",
    "salsa",
    "Hip Hop",
    "Ballet",
    "Breakdance",
    "Regatton",
    "Afrobeat",
    "Cumbia",
    "Merengue"
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        options=options,
        levels=levels,
        danceTypes=danceTypes
    )


@app.route("/select", methods=["POST"])
def select():

    data = request.get_json()
    option = data["option"]

    show_add_form = False
    show_field = False

    if option == options[0]:
        message = "Participant 1, 2, 3."

    elif option == options[1]:
        message = "Participants 1, 2, 3."

    elif option == options[2]:
        message = "Participants 1, 2, 3."

    elif option == options[3]:
        message = "Enter the new participant's information."
        show_add_form = True

    elif option == options[4]:
        message = "Remove a participant."

    elif option == options[5]:
        message = "Remove participants without subscription."

    elif option == options[6]:
        message = "Number of participants in each level."

    elif option == options[7]:
        message = "Participants for each dance type."

    elif option == options[8]:
        message = "Participants for a specific dance type."

    else:
        message = "Please select an option."

    return {
        "message": message,
        "show_field": show_field,
        "show_add_form": show_add_form
    }


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name")
    age = request.form.get("age")
    birthday = request.form.get("birthday")
    gender = request.form.get("gender")
    level = request.form.get("level")
    danceType = request.form.get("danceType")

    return f"""
        <h1>Participant Added</h1>

        <p><strong>Name:</strong> {name}</p>
        <p><strong>Age:</strong> {age}</p>
        <p><strong>Date of Birth:</strong> {birthday}</p>
        <p><strong>Gender:</strong> {gender}</p>
        <p><strong>Level:</strong> {level}</p>
        <p><strong>Dance Type:</strong> {danceType}</p>

        <br>

        <a href="/">Return to home</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
