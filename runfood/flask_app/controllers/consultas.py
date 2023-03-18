from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.paciente import Paciente
from flask_app.models.doctor import Doctor
from flask_app.models.consulta import Consulta

@app.route('/odonto/agendarse')
def pagendarse():
    if 'user_name' in session:
        return render_template('agendarse.html',user=session['user_name'], tratamientos=)
    else:
        flash('Tienes que iniciar sesión!')
        return redirect('/odonto')
    
@app.route('/odonto/agendarse/procesar', methods=['POST'])
def reservar(data):
    if 'user_id' in session:
        data={
            "id_paciente": session['user_id'],
            "id_doctor": request.form["id_doctor"],
            "consulta": request.form["consulta"],
            "fecha": request.form["fecha"],
            "comentarios": request.form["comentarios"]
        }
        check=Consulta.check(data)
        if not check:
            flash("Horario no disponible")
            return redirect("/odonto/agendarse")
        else:
            Consulta.agendar(data)
            flash("Agendamiento realizado correctamente")
            return redirect('/odonto')
    else:
        flash('Tienes que iniciar sesión para poder agendar citas')
        return redirect('/login')
    
