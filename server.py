import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "Hi python"


if __name__ == '__main__':
    app.run(port=8080, host='127.1.0.0')
