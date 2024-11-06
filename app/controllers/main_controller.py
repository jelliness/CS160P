from flask import render_template, jsonify
from app import app
import sklearn
from app.models.model import predict_class 

@app.route('/main')
def main_page():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    # List of fields that should not be empty or null
    required_fields = [
        'education', 'income', 'kidhome', 'teenhome', 'recency', 'wines', 'fruits', 'meat',
        'fish', 'sweets', 'gold', 'num_deals_purchases', 'num_web_purchases', 'num_catalog_purchases',
        'num_store_purchases', 'num_web_visits_month', 'accepted_cmp3', 'accepted_cmp4', 'accepted_cmp5',
        'accepted_cmp1', 'accepted_cmp2', 'complain', 'response', 'customer_for', 'age', 'spent',
        'living_with', 'children', 'family_size', 'is_parent', 'total_promos'
    ]

    result = predict_class(required_fields)

    return render_template("result.html", customer_type=result[0])