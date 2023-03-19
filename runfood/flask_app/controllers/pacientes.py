from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.doctor import Doctor
from flask_app.models.paciente import Paciente


@app.route('/new/paciente')
def new_paciente():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_paciente.html',user=Paciente.get_by_id(data))


@app.route('/create/paciente',methods=['POST'])
def create_paciente():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Paciente.validate_pacientes(request.form):
        return redirect('/new/paciente')
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "ci_ruc": request.form["ci_ruc"],
        "direccion": request.form["direccion"],
        "nro_telefono": request.form["nro_telefono"],
        "fecha_nacimiento": request.form["fecha_nacimiento"],
        "sexo": request.form["sexo"],
        "patologia": request.form["patologia"],
        "created_at": request.form["created_at"],
        "id_doctor": session["user_id"]
    }
    Paciente.save(data)
    return redirect('/dashboard')

@app.route('/edit/paciente/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    paciente_data = {
        "id":session['user_id']
    }
    return render_template("edit_paciente.html",edit=Paciente.get_one(data))

@app.route('/update/paciente',methods=['POST'])
def update_paciente():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Paciente.validate_pacientes_updated(request.form):
        data = {
        "id": request.form['id']
    }
        print('Data:', data)
        return render_template('/edit/paciente/', edit=Paciente.get_one(data))
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "ci_ruc": request.form["ci_ruc"],
        "direccion": request.form["direccion"],
        "nro_telefono": request.form["nro_telefono"],
        "fecha_nacimiento": request.form["fecha_nacimiento"],
        "sexo": request.form["sexo"],
        "patologia": request.form["patologia"],
        "created_at": request.form["created_at"],
        "id_doctor": session["user_id"]
    }
    Paciente.update(data)
    return redirect('/dashboard')

@app.route('/paciente/<int:id>')
def show_updated(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    paciente_data = {
        "id":session['user_id']
    }
    return render_template("show_paciente.html",paciente=Paciente.get_one(data),paciente=Paciente.get_by_id(paciente_data))

@app.route('/destroy/paciente/<int:id>')
def destroy_paciente(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Paciente.destroy(data)
    return redirect('/dashboard')

