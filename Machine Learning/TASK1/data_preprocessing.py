import pandas as pd

def load_data(file_path):
    """Load the dataset from CSV."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Select relevant features and handle missing values."""
    features = ['GrLivArea', 'BedroomAbvGr', 'FullBath']
    target = 'SalePrice'

    # Select features and target
    X = data[features]
    y = data[target]

    # Handle missing values
    X = X.fillna(X.mean())
    
    return X, y
