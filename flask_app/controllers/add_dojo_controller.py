from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def display_dojo():
    list_of_dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", list_dojos=list_of_dojos)

@app.route('/dojos', methods=['POST'])
def update_dojos( id ):
    Dojo.create_dojo( id )
    return redirect("/dojos/<int:id>")

@app.route('/dojos/<int:id>')
def display_one_dojo( id ):
    one_dojo = {
        "id" : id
    }
    selected_dojo = Dojo.get_dojo_by_id( one_dojo )
    list_of_ninjas = Ninja.get_ninja_by_id( one_dojo )
    
    return render_template("dojo_meta.html", selected_dojo = selected_dojo, list_of_ninjas = list_of_ninjas)

@app.route("/ninjas")
def display_ninja_form():
    list_of_dojos = Dojo.get_all_dojos()
    
    return render_template("ninja.html", list_of_dojos = list_of_dojos)

@app.route("/ninjas", methods="POST")
def add_new_ninja():
    ninja_baby = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    
    Ninja.create_ninja(ninja_baby)
    
    return redirect('/dojos/<int:id>')
