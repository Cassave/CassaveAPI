from flask import Flask
from flask_cors import CORS

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello"


@app.route("/predict")
def predict():
    return "Cassava Green Mite"


if __name__ == "__main__":
    app.run(debug=True)
