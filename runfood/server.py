from flask_app import app
from flask_app.controllers import doctores, pacientes, transactions, consultas

if __name__=='__main__':
    app.run(debug=True)
