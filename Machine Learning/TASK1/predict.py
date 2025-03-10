import pickle
import numpy as np

# Load trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

def predict_price(grlivarea, bedrooms, fullbath):
    """Predicts house price based on input features."""
    input_data = np.array([[grlivarea, bedrooms, fullbath]])
    predicted_price = model.predict(input_data)
    return predicted_price[0]

# Example usage
if __name__ == "__main__":
    area = float(input("Enter living area (sq ft): "))
    beds = int(input("Enter number of bedrooms: "))
    baths = int(input("Enter number of full bathrooms: "))

    price = predict_price(area, beds, baths)
    print(f"Predicted House Price: ${price:.2f}")
