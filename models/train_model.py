import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    "vehicles": [50, 100, 150, 200, 300],
    "congestion": [30, 70, 120, 180, 260]
}

df = pd.DataFrame(data)

X = df[["vehicles"]]
y = df["congestion"]

model = LinearRegression()
model.fit(X, y)

# save model in models folder
pickle.dump(model, open("models/traffic_model.pkl", "wb"))

print("Model trained and saved")