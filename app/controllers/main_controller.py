from flask import render_template, request, redirect, url_for
from app import app
from app.models.metrics import compute_metrics, interpret_accuracy

@app.route('/main')
def main_page():
    return render_template('main.html')

@app.route('/compute', methods=['POST'])
def compute():
    try:
        TP = float(request.form['TP'])
        TN = float(request.form['TN'])
        FP = float(request.form['FP'])
        FN = float(request.form['FN'])
        
        if TP < 0 or TN < 0 or FP < 0 or FN < 0:
            raise ValueError("Values cannot be negative.")
        
        precision, recall, f1_score, accuracy, total = compute_metrics(TP, TN, FP, FN)
        
        interpretation = interpret_accuracy(accuracy)
        
        return render_template('main.html', precision=precision, recall=recall, f1_score=f1_score, accuracy=accuracy, total=total, interpretation=interpretation)
    except (ValueError, KeyError):
        error_message = "There was an error in Computing for the Classification Metrics, please click the back button to go back to the Main Page and provide a correct input."
        return render_template('error.html', error_message=error_message, back_url=url_for('main_page'))
