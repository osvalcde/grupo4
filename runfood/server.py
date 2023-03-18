from flask_app import app
from flask_app.controllers import clietes, pacientes, transactions

if __name__=='__main__':
    app.run(debug=True)
