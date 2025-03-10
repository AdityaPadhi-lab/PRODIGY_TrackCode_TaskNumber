import pickle
from sklearn.metrics import mean_squared_error, r2_score
from data_preprocessing import load_data, preprocess_data

# Load model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load and preprocess data
data = load_data("train.csv")
X, y = preprocess_data(data)

# Predict and Evaluate
y_pred = model.predict(X)

print(f"Mean Squared Error: {mean_squared_error(y, y_pred)}")
print(f"R² Score: {r2_score(y, y_pred)}")
