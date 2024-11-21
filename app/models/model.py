from flask import jsonify
import pickle
import numpy as np

def predict_class(data):
    # Load the model using pickle
    with open(r'./app/models/bagged_random_forest.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
        
    # Convert data list to numpy array for prediction
    input_data = np.array([data]).astype(float)

    # Predict customer type
    prediction = model.predict(input_data)
    return prediction[0]  # Return the first prediction directly