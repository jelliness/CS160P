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

    # List of fields that should not be empty or null, excluding 'children'
    required_fields = [
        'education', 'income', 'kidhome', 'teenhome', 'recency', 'wines', 'fruits', 'meat',
        'fish', 'sweets', 'gold', 'num_deals_purchases', 'num_web_purchases', 'num_catalog_purchases',
        'num_store_purchases', 'num_web_visits_month', 'accepted_cmp3', 'accepted_cmp4', 'accepted_cmp5',
        'accepted_cmp1', 'accepted_cmp2', 'complain', 'response', 'customer_for', 'age', 'spent',
        'living_with', 'is_parent', 'total_promos'
    ]

    # Check for missing fields
    missing_fields = [field for field in required_fields if field not in data or data[field] is None]
    if missing_fields:
        return jsonify({'error': f'Missing or empty value for {missing_fields}'}), 400

    # Calculate 'children' as an integer based on 'kidhome' and 'teenhome'
    children = int(data['kidhome']) + int(data['teenhome'])
    
    # Extract values in the required order, inserting 'children' before 'family_size'
    ordered_values = [
        data[field] for field in required_fields[:24]
    ] + [children] + [data['family_size']] + [
        data[field] for field in required_fields[24:]
    ]

    print("Ordered data values:", ordered_values)

    # Pass the JSON data to predict_class
    prediction_result = predict_class(ordered_values)

    # Check if predict_class returned an error response
    if isinstance(prediction_result, tuple):  # Means there was an error in predict_class
        return prediction_result  # This will return the error response directly

    # Render the result template with the prediction result
    return render_template("result.html", customer_type=str(prediction_result))