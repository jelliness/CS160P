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
    
    characteristic = ""
    if str(prediction_result) == "high spending & average income":
        characteristic = "Individuals or households in this group likely have a balanced lifestyle. While their income is average, they tend to spend relatively more, possibly on maintaining a particular lifestyle or fulfilling aspirational needs."
        image_path = "3.png"
    elif str(prediction_result) == "low spending & low income":
        characteristic = "These individuals or households often face financial constraints and adopt a frugal approach to spending, focusing on necessities while minimizing discretionary expenses."
        image_path = "1.png"
    elif str(prediction_result) == "high spending & high income":
        characteristic = "These individuals or households enjoy substantial financial freedom. Their high income allows for considerable spending on both necessities and luxury items, reflecting a focus on comfort and premium experiences."
        image_path = "4.png"
    elif str(prediction_result) == "high spending & low income":
        characteristic = "These individuals or households typically have high disposable income and spend freely on luxury goods, services, and experiences. They may prioritize quality and exclusivity over cost."
        image_path = "2.png"

    print(image_path)
    # Render the result template with the prediction result
    return render_template("result.html", customer_type=str(prediction_result), insight=(characteristic),  path=image_path)