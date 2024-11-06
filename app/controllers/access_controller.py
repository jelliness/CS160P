from flask import render_template, request, redirect, url_for
from app import app
from app.models.user import authenticate

@app.route('/')
def access_page():
    return render_template('access.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if authenticate(username, password):
        return redirect(url_for('main_page'))
    else:
        error_message = "There was an error in Accessing the Main Page, please click the back button to go back to the Access Page and provide a correct credential"
        return render_template('error.html', error_message=error_message, back_url=url_for('access_page'))
