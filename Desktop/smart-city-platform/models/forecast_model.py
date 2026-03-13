import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("data/traffic_data.csv")

X = data[["vehicles"]]
y = data["congestion"]

model = LinearRegression()
model.fit(X,y)

pickle.dump(model,open("models/forecast_model.pkl","wb"))

print("Forecast model trained")