from flask import render_template, request, jsonify
from app import app
import pickle
import numpy as np
import sklearn

# Load the model (assuming it's in the same directory; adjust the path if needed)
with open(r'./app/controllers/adaboost_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/main')
def main_page():
    return render_template('main.html')

@app.route('/compute', methods=['POST'])
def compute():
    # Fetch data from form and convert to the appropriate types if necessary
    form_data = {
        'education': int(request.form.get('education')),
        'income': float(request.form.get('income')),
        'kidhome': int(request.form.get('kidhome')),
        'teenhome': int(request.form.get('teenhome')),
        'recency': int(request.form.get('recency')),
        'wines': int(request.form.get('wines')),
        'fruits': int(request.form.get('fruits')),
        'meat': int(request.form.get('meat')),
        'fish': int(request.form.get('fish')),
        'sweets': int(request.form.get('sweets')),
        'gold': int(request.form.get('gold')),
        'num_deals_purchases': int(request.form.get('num_deals_purchases')),
        'num_web_purchases': int(request.form.get('num_web_purchases')),
        'num_catalog_purchases': int(request.form.get('num_catalog_purchases')),
        'num_store_purchases': int(request.form.get('num_store_purchases')),
        'num_web_visits_month': int(request.form.get('num_web_visits_month')),
        'accepted_cmp3': int(request.form.get('accepted_cmp3')),
        'accepted_cmp4': int(request.form.get('accepted_cmp4')),
        'accepted_cmp5': int(request.form.get('accepted_cmp5')),
        'accepted_cmp1': int(request.form.get('accepted_cmp1')),
        'accepted_cmp2': int(request.form.get('accepted_cmp2')),
        'complain': int(request.form.get('complain')),
        'response': int(request.form.get('response')),
        'customer_for': int(request.form.get('customer_for')),
        'age': int(request.form.get('age')),
        'spent': float(request.form.get('spent')),
        'living_with': int(request.form.get('living_with')),
        'children': int(request.form.get('children')),
        'family_size': int(request.form.get('family_size')),
        'is_parent': int(request.form.get('is_parent')),
        'total_promos': int(request.form.get('total_promos'))
    }

    # Convert form data to array for prediction
    input_data = np.array([list(form_data.values())]).astype(float)

    # Predict customer type
    prediction = model.predict(input_data)

    # Return prediction as JSON response
    return jsonify({"customer_type": prediction[0]})
