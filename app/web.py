from flask import request, jsonify, Response, json, redirect, abort, render_template, session, json
from app import app, get_db

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'GET':
        return render_template("volunteer.html")
    else:
        # save details
        return render_template("thanks.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Do search
        return render_template("results.html")
    else:
        return render_template("search.html")

@app.route('/contact', methods=['POST'])
def contact():
    # send email
    # register contact
    return render_template('contact_done.html')
