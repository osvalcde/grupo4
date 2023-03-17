from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.pensamiento import Pensamiento
from flask_app.models.user import User


@app.route('/new/pensamiento')
def new_pensamiento():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_pensamiento.html',user=User.get_by_id(data))


@app.route('/create/pensamiento',methods=['POST'])
def create_pensamiento():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Pensamiento.validate_pensamientos(request.form):
        return redirect('/new/pensamiento')
    data = {
        "descripcion": request.form["descripcion"],
        "created_at": request.form["created_at"],
        "idUsuario": session["user_id"]
    }
    Pensamiento.save(data)
    return redirect('/dashboard')

@app.route('/edit/pensamiento/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_pensamiento.html",edit=Pensamiento.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/pensamiento',methods=['POST'])
def update_pensamiento():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Pensamiento.validate_pensamientos_updated(request.form):
        data = {
        "id": request.form['id']
    }
        print('Data:', data)
        return render_template('/edit/pensamiento/', edit=Pensamiento.get_one(data))
    data = {
        "descripcion": request.form["descripcion"],
        "id": request.form['id']
    }
    Pensamiento.update(data)
    return redirect('/dashboard')

@app.route('/pensamiento/<int:id>')
def show_updated(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_pensamiento.html",pensamiento=Pensamiento.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/pensamiento/<int:id>')
def destroy_pensamiento(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Pensamiento.destroy(data)
    return redirect('/dashboard')

