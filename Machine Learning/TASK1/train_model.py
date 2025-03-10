import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from data_preprocessing import load_data, preprocess_data

import sklearn
print(sklearn.__version__)

# Load and preprocess data
data = load_data("train.csv")
X, y = preprocess_data(data)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

# Evaluate Model
y_pred = model.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"R² Score: {r2_score(y_test, y_pred)}")
