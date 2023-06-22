import os
# importing flask class
from flask import Flask, render_template

# creating an instance of Flask class and soring it in name variable called name- a build in python variable(templates and static files)
app = Flask(__name__)

# app root decorator(py notation) a way of wrapping functions. if we try to browse through the rout directory indicated by "/" - the functions underneath is triggerd
@app.route("/")
def index():
    return render_template("index.html")

# app route are called views- the route to the link page
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) # never do debug=True in a production app or project submitted for assesment, only in dev stages, change to false if submitting
    

   
