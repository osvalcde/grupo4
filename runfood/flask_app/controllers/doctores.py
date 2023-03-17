from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.paciente import Paciente
from flask_app.models.doctor import Doctor
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():

    if not Doctor.validate_register(request.form):
        return redirect('/')
    data ={ 
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "ruc": request.form['ruc'],
        "telefono": request.form['telefono'],
        "observacion": request.form['observacion'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = Doctor.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login',methods=['POST', 'GET'])
def login():
    if (request.form.get('email') == '') or (request.form.get('password') == ''):
        flash("email o password invalido!","login")
    else:
        data = {
            'email':request.form.get('email')
        }
        user = Doctor.get_by_email(data)
        if not user:
            flash("Email invalido","login")
            return redirect('/')
        if not bcrypt.check_password_hash(user.password, request.form['password']):
            flash("Password invalido","login")
            return redirect('/')
        session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=Doctor.get_by_id(data),paciente=Paciente.get_all())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
