from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Fetch avatars from Reqres API
    response = requests.get("https://reqres.in/api/users?page=1")
    users = response.json().get("data", [])

    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)