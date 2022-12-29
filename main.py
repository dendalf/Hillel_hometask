from flask import Flask
import utils

app = Flask(__name__)


@app.route("/avr_data")
def get_avr_data():
    return utils.calculate_data()


app.run(debug=True)
