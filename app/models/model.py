from flask import request, jsonify
import pickle
import numpy as np
import sklearn
    
def predict_class(required_fields):
    # Load the model using pickle
    with open(r'./app/controllers/adaboost_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
        
    # Fetch form data and check for missing or empty fields
    form_data = {}
    for field in required_fields:
        value = request.form.get(field)
        if value is None or value.strip() == "":  # Check for null or blank
            return jsonify({"error": f"Missing or empty value for {field}"}), 400
        # Convert to appropriate type
        if field in ['income', 'spent']:  # For float fields
            form_data[field] = float(value)
        else:  # For integer fields
            form_data[field] = int(value)

    # Convert form data to array for prediction
    input_data = np.array([list(form_data.values())]).astype(float)

    # Predict customer type
    prediction = model.predict(input_data)
    return prediction