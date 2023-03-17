from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Paciente:
    db_name = 'odonto'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.nombre = db_data['nombre']
        self.apellido = db_data['apellido']
        self.ci_ruc = db_data['ci_ruc']
        self.direccion = db_data['direccion']
        self.nro_telefono = db_data['nro_telefono']
        self.fecha_nacimiento = db_data['fecha_nacimiento']
        self.sexo = db_data['sexo']
        self.patologia = db_data['patologia']
        self.created_at = db_data['created_at']
        self.updated_at=  db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = """INSERT INTO pacientes (nombre, apellido, ci_ruc, direccion,nro_telefono,fecha_nacimiento,sexo,patologia, created_at, updated_at) 
        VALUES (%(nombre)s,%(apellido)s,%(ci_ruc)s,%(direccion)s,%(nro_telefono)s,%(fecha_nacimiento)s,%(sexo)s,%(patologia)s,NOW(),NOW());"""
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pacientes;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_pacientes = []
        for row in results:
            print(row['created_at'])
            all_pacientes.append( cls(row) )
        return all_pacientes
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM pacientes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = """UPDATE pacientes SET nombre=%(nombre)s, apellido=%(apellido)s,ci_ruc=%(ci_ruc)s,direccion=%(direccion)s, 
        nro_telefono=%(nro_telefono)s,fecha_nacimiento=%(fecha_nacimiento)s,sexo=%(sexo)s,patologia=%(patologia)s,updated_at=NOW() WHERE id = %(id)s;"""
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM pacientes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_pacientes(pacientes):
        is_valid = True
        if len(pacientes['nombre']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","paciente")
        if pacientes['created_at'] == "":
            is_valid = False
            flash("Please enter a date","paciente")
        return is_valid
