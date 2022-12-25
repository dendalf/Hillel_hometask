from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def print_requirements():
    return utils.read_file()


app.run(debug=True)
