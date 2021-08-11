#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
import requests
from flask import render_template

app = Flask(__name__)

jsonrequest = {
    "question": "What is the meaning of life, the universe, and everything?",
    "nm": 42
}

html= """<style>
body {
  background-color: black;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<h1>TRIVIA TIME</h1>
<p>What is the meaning of life, the universe, and everything?</p>
<img src="https://stevetobak.com/wp-content/uploads/2021/02/dont-panic.png" alt="Avatar" style="width:200px">

    <form action = "/login" method = "POST">
        <p><input type = "text" name = "nm"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>

</body>
</html>"""

@app.route("/correct")
def success():
    return f"That is correct!"

@app.route("/")
def start():
    return html

@app.route("/json")
def jsonstart():
    x = requests.post( "http://localhost:5000/json" , jsonrequest.get("question", "nothing is there"))

    return x

@app.route("/login", methods = ["POST"])
def login():

    if request.json:
        data= request.json
        if data["nm"] == "42":
            return redirect("/correct")
        else:
            return redirect("/")

    if request.form.get("nm"):
        answer = request.form.get("nm")
        if answer == "42":
            return redirect("/correct")
        else:
            return redirect("/")
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000) # runs the application
