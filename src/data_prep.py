import pandas as pd

def load_data(path):
    """Load CSV and select required columns."""
    df = pd.read_csv(path)
    cols = ['GrLivArea', 'BedroomAbvGr', 'FullBath', 'SalePrice']
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")
    return df[cols].copy()

def clean_data(df):
    """Simple cleaning: drop rows with missing values and remove extreme GrLivArea outliers."""
    df = df.dropna(subset=['GrLivArea', 'BedroomAbvGr', 'FullBath', 'SalePrice'])
    # Remove extreme GrLivArea outliers (top 1%)
    df = df[df['GrLivArea'] < df['GrLivArea'].quantile(0.99)]
    return df
