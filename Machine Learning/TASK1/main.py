from train_model import model
from predict import predict_price

def main():
    print("Welcome to the House Price Predictor")
    area = float(input("Enter living area (sq ft): "))
    beds = int(input("Enter number of bedrooms: "))
    baths = int(input("Enter number of full bathrooms: "))

    price = predict_price(area, beds, baths)
    print(f"Estimated House Price: ${price:.2f}")

if __name__ == "__main__":
    main()
