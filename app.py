from flask import Flask, render_template, request

from model import model

# creating an object of flask
app = Flask(__name__)

# defining routes in order to direct to various pages as per the values in parantheses
# @app.route("/")
# def hello():
#     return "First Page"

# make sure you have different function names to check the working of app
@app.route("/hey")
def he():
    return "hey"

# as we have to display stuff properly we use render templates where we will show desired things using html and css
@app.route("/")
def webage():
    return render_template("index.html")

# function to submit data
# we are connecting the form to the route using the action over there
@app.route("/sub", methods = ["POST"])
def submit():
    if request.method == "POST":
        # this will take input form user side 
        input = request.form["level"]
        # predict the value
        output = model(input)[0]


    # .py->html
    # pass the predicted value 
    return render_template("submit.html",pos = input, prediction = int(round(output)))


# below code indicates that if we are running the current file then run the app
# debug mode allows us to make changes which would refelct on the webpage
if __name__ == "__main__":
    app.run(debug = True) 