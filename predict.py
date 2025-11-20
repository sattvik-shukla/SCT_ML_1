import pickle
import pandas as pd

# Load the model
model_path = "models/linear_regression.pkl"
model = pickle.load(open(model_path, "rb"))

# Example input
sample = pd.DataFrame([{
    "GrLivArea": 1500,
    "BedroomAbvGr": 3,
    "FullBath": 2
}])

# Predict
prediction = model.predict(sample)[0]

print("Predicted SalePrice:", prediction)
