from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# load models
traffic_model = pickle.load(open("models/traffic_model.pkl","rb"))
forecast_model = pickle.load(open("models/forecast_model.pkl","rb"))

# load dataset
traffic_data = pd.read_csv("data/traffic_data.csv").dropna()


@app.route("/")
def home():
    return "Smart City AI Platform Running"


# traffic prediction
@app.route("/predict_traffic",methods=["POST"])
def predict_traffic():

    data = request.json
    vehicles = int(data["vehicles"])

    prediction = traffic_model.predict([[vehicles]])

    return jsonify({
        "predicted_congestion": float(prediction[0])
    })


# traffic dataset analytics
@app.route("/traffic_stats")
def traffic_stats():

    vehicles = traffic_data["vehicles"].tolist()
    congestion = traffic_data["congestion"].tolist()

    return jsonify({
        "vehicles": vehicles,
        "congestion": congestion
    })


# future traffic forecast
@app.route("/forecast",methods=["POST"])
def forecast():

    data = request.json
    vehicles = int(data["vehicles"])

    prediction = forecast_model.predict([[vehicles]])

    return jsonify({
        "future_congestion": float(prediction[0])
    })


if __name__ == "__main__":
    app.run(debug=True)