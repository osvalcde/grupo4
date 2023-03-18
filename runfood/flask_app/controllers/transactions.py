from flask import render_template,redirect,session,request, flash
from flask_app import app

######################################
from flask_app.models.transaction import Transaction
from datetime import date

#######################################################################
###TRANSACTIONS

#SEE TRANSACTIONS
@app.route('/transacciones')
def derby():
    return render_template('transaction_new.html', all_transactions=Transaction.get_all_LD(), 
        all_doctors=Transaction.get_all_doctors_LD(), today=date.today(), total=Transaction.get_total_LD())

#ADD TRANSACTION
@app.route('/add_transaction', methods=['POST'])
def add():
    if not Transaction.validate_B(request.form):
        return redirect("/transacciones")
    Transaction.save_N(request.form)
    return redirect('/transacciones')

#DELETE TRANSACTION
@app.route('/transacciones/delete/<int:id>')
def destroy(id):
    data ={'id': id}
    Transaction.destroy(data)
    return redirect('/transacciones')

#UPDATE TRANSACTION
@app.route('/transacciones/edit/<int:id>')
def edit(id):
    data_D = { "id" : id }
    return render_template('transaction_edit.html', all_transactions=Transaction.get_all_LD(), 
        all_doctors=Transaction.get_all_doctors_LD(), today=date.today(), transaction_to_edit=Transaction.get_one_C(data_D))

@app.route('/transacciones/edit', methods=['POST'])
def update():
    if not Transaction.validate_B(request.form):
        return redirect("/transacciones/edit/"+str(request.form['id']))
    Transaction.update(request.form)
    return redirect('/transacciones')

#FUNCIONES AUXILIARES PARA LOS CONTROLADORES
def validate_logged_in():   #Verifica si el usuario ingresó a la sesión, sino le redirige a la página de ingreso
    if 'user_id' not in session:
        return redirect('/logout')