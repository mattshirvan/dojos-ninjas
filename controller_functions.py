from flask import render_template, redirect, request, session, flash
from config import db
from models import Dojo, Ninja

def index():
    dojos = Dojo.query.all()
    return render_template("index.html", dojos = dojos)

def add():
    if request.form['add'] == 'add_dojo':  
        new_dojo = Dojo(name = request.form['name'], city = request.form['city'], state = request.form['state'])
        db.session.add(new_dojo)
    elif request.form['add'] == 'add_ninja':
        new_ninja = Ninja(first_name = request.form['first_name'], last_name = request.form['last_name'], dojo_id = request.form['dojo'])
        db.session.add(new_ninja)
    db.session.commit()
    return redirect("/")