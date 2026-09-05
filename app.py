from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    options = ["View participants", "View details", "View participant details",
               "add participant","remove participant","clear","remove participants without subscription",
               "number of participants in each level","participants for each dance type",
               "participants for a specific dance type","exit"
               ]
    return render_template("index.html", options=options)


@app.route("/select", methods=["POST"])
def select():
    data = request.get_ison() 
    option = data["option"]
    data = request.get_json() 
    option = data["option"]
    if option == option[0]:
        message = "Participant 1, 2, 3."
    elif option==option[1]:
        message = "participants 1,2,3"
    elif option == option[2]:
        message = "participants 1,2,3,"
    elif option == option[3]:
        message = "add a participant"
    elif option == option[4]:
        message = "remove a participant"
    elif option == option[5]:
        message =  "clear"
    elif option == option[6]:
        message = "remove participants without subscription"
    elif option == option[7]:
        message = "number of participants in each level"
    elif option == option[8]:
        message = "participants for each dance type"
    elif option == option[9]:
        message = "participants for a specific dance type"
    elif option == option[10]:
        message = "exit"
    else:
        message = "please select an option"
    return {"message":message}
    
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    return f"Name: {name}<br>Email: {email}"

app.run(debug=True)
