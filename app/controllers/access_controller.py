from flask import render_template, request, redirect, url_for
from app import app

@app.route('/')
def access_page():
    return render_template('access.html')

@app.route('/start', methods=['POST'])
def start():
    return redirect(url_for('main_page'))