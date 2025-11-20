# src/train_model.py
import os
import pickle
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from data_prep import load_data, clean_data

def evaluate(y_true, y_pred):
    """Return MAE, RMSE, R2. Handles sklearn versions that don't accept squared=False."""
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = math.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    return {'MAE': mae, 'RMSE': rmse, 'R2': r2}

def train_and_save_model(data_path, model_path):
    print(f"Loading data from: {data_path}")
    df = load_data(data_path)
    df = clean_data(df)
    print(f"Data shape after cleaning: {df.shape}")

    X = df[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
    y = df['SalePrice']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics = evaluate(y_test, y_pred)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    print("Training complete. Metrics:")
    for k, v in metrics.items():
        print(f"  {k}: {v:.2f}")

    # return metrics and some test data for optional analysis
    return metrics, model, (X_test, y_test, y_pred)

if __name__ == '__main__':
    DATA_PATH = os.path.join('data', 'raw', 'train.csv')
    MODEL_PATH = os.path.join('models', 'linear_regression.pkl')

    metrics, model, test_data = train_and_save_model(DATA_PATH, MODEL_PATH)
