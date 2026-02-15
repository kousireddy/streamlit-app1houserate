import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# User input
area = float(input("Enter area: "))
bed = int(input("Enter bedrooms: "))
bath = int(input("Enter bathrooms: "))

prediction = model.predict([[area, bed, bath]])

print("Predicted House Price:", prediction[0])
