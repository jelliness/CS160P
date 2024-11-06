from flask import render_template, jsonify, request
from app import app
import sklearn
from app.models.model import predict_class 

@app.route('/main')
def main_page():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid or missing JSON data'}), 400

    # List of fields that should not be empty or null
    required_fields = [
        'education', 'income', 'kidhome', 'teenhome', 'recency', 'wines', 'fruits', 'meat',
        'fish', 'sweets', 'gold', 'num_deals_purchases', 'num_web_purchases', 'num_catalog_purchases',
        'num_store_purchases', 'num_web_visits_month', 'accepted_cmp3', 'accepted_cmp4', 'accepted_cmp5',
        'accepted_cmp1', 'accepted_cmp2', 'complain', 'response', 'customer_for', 'age', 'spent',
        'living_with', 'children', 'family_size', 'is_parent', 'total_promos'
    ]

    missing_fields = [field for field in required_fields if field not in data or data[field] is None]
    if missing_fields:
        return jsonify({'error': f'Missing or empty value for {missing_fields}'}), 400
    
    # Pass the data to predict_class (ensure that predict_class returns the correct format)
    
    prediction_result = predict_class([data[field] for field in required_fields])
    print(prediction_result)
    # Ensure prediction_result is a string or type that can be displayed
    if not isinstance(prediction_result, str):
        prediction_result = str(prediction_result)
    
    # Return the rendered result template
    return render_template("result.html", customer_type=prediction_result)
