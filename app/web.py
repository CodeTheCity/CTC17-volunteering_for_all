from flask import request, jsonify, Response, json, redirect, abort, render_template, session
from app import app, db, Volunteer, Charity, Category, Skill, Task, Match

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'GET':
        return render_template("volunteer.html")
    else:
        # save details
        v = Volunteer(
            email=request.form["email"],
            bio=request.form["message"]
        )
        db.session.add(v)
        db.session.commit()
        # TODO: save skills and category interest
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
