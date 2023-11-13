from random import randint
from flask import Flask

app = Flask(__name__)

@app.route("/server_request")
def server_request():
    return "served"

if __name__ == "__main__":
    app.run(port=8080, debug=True)