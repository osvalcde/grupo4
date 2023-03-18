from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from datetime import date, datetime
import inspect      #sirve para poder acceder al nombre de un método dentro del mismo, pudiendo servir para imprimirlo y detectar errores

schema_name="odonto"

class Transaction:
    def __init__(self, data):
        self.id = data['id']
        self.fecha = data['fecha']
        self.monto = data['monto']
        self.concepto = data['concepto']
        self.id_doctor = data['id_doctor']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.lista=[]   #aún no sé lista de qué será

    #VALIDACIONES
    @classmethod    #Debería ser @staticmethod porque no necesito pasarle cls o self pero uso @classmethod para poder rastrear el paso 
                    #   por este Método
    def validate_B(cls, user_D):
        is_valid = True # asumimos que esto es true
        return is_valid

    #INSERT QUERIES
    @classmethod
    def save_N(cls, data_D):
        query = "INSERT INTO gastos (fecha, monto, concepto, id_doctor, created_at, updated_at) \
            VALUES (%(fecha)s, %(monto)s, %(concepto)s, %(id_doctor)s, NOW(), NOW());"
        result_N = connectToMySQL(schema_name).query_db(query, data_D)
        print("save_N TRANSACTION\n")
        return result_N

    #SELECT QUERIES
    @classmethod    #usar @classmethod siempre que consulte a la base de datos
    def get_all_LD(cls):
        query = "SELECT * FROM gastos \
            LEFT JOIN doctores ON gastos.id_doctor=doctores.id;"
        results_LD = connectToMySQL(schema_name).query_db(query)
        if len(results_LD)==0:
            results_LD=[{'id':"", 'fecha':"", 'monto':"", 'concepto':"", 'id_doctor':"", 'nombre':'', 'apellido':''}]
        print(results_LD)
        print("get_all_LD TRANSACTION\n")
        return results_LD
    
    #SELECT QUERIES
    @classmethod    #usar @classmethod siempre que consulte a la base de datos
    def get_total_LD(cls):
        query = "SELECT SUM(monto) as 'total' FROM gastos WHERE id>0;"
        results_LD = connectToMySQL(schema_name).query_db(query)
        if len(results_LD)==0:
            results_LD=[{'total':0}]
        print(results_LD[0]['total'])
        print("get_total_LD TRANSACTION\n")
        return results_LD[0]['total']

    #VERIFICAR!!!!!!!!!!!!!!!!!!!1
    #SELECT QUERIES
    @classmethod    #usar @classmethod siempre que consulte a la base de datos
    def get_total_by_dr_LD(cls, data_D):
        query = "SELECT id_doctor, SUM(monto) as 'total' FROM gastos WHERE id_doctor;"
        results_LD = connectToMySQL(schema_name).query_db(query, data_D)
        if len(results_LD)==0:
            results_LD=[{'total':0}]
        print(results_LD)
        print("get_total_by_dr_LD TRANSACTION\n")
        return results_LD

    @classmethod
    def get_one_C(cls, data_D):
        query  = "SELECT * FROM gastos WHERE id = %(id)s;"
        results_LD = connectToMySQL(schema_name).query_db(query, data_D)
        return cls(results_LD[0])

    #UPDATE QUERIES
    @classmethod
    def update(cls, data_D):
        query = "UPDATE gastos SET fecha=%(fecha)s, monto=%(monto)s, concepto=%(concepto)s, id_doctor=%(id_doctor)s, \
            updated_at=NOW() WHERE id = %(id)s;"
        print("update TRANSACTION\n")
        return connectToMySQL(schema_name).query_db(query, data_D)

    #DELETE QUERIES
    @classmethod
    def destroy(cls, data_D):
        query  = "DELETE FROM gastos WHERE id = %(id)s;"
        print("destroy TRANSACTION\n")
        return connectToMySQL(schema_name).query_db(query, data_D)

    #DOCTORS!!!!!!!!!!!!!!
    #SELECT QUERIES
    @classmethod    #usar @classmethod siempre que consulte a la base de datos
    def get_all_doctors_LD(cls):
        query = "SELECT * FROM doctores;"
        results_LD = connectToMySQL(schema_name).query_db(query)
        print(results_LD)
        print("get_all_doctors_LD TRANSACTION\n")
        return results_LD