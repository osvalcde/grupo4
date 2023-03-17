from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Doctor:
    db_name = "odonto"
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.ruc = data['ruc']
        self.telefono = data['telefono']
        self.observacion = data['observacion']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']

    @classmethod
    def save(cls,data):
        query = """INSERT INTO doctores (nombre,apellido,ruc,telefono,observacion,email,password,created_at) 
        VALUES(%(nombre)s,%(apellido)s,%(ruc)s,%(telefono)s,%(observacion)s,%(email)s,%(password)s, NOW())"""
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM doctores;"
        results = connectToMySQL(cls.db_name).query_db(query)
        doctores = []
        for row in results:
            doctores.append( cls(row))
        return doctores

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM doctores WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM doctores WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_register(doctor):
        is_valid = True
        query = "SELECT * FROM doctores WHERE email = %(email)s;"
        results = connectToMySQL(Doctor.db_name).query_db(query,doctor)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(doctor['email']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if len(doctor['nombre']) < 3:
            flash("First name must be at least 3 characters","register")
            is_valid= False
        if len(doctor['apellido']) < 3:
            flash("Last name must be at least 3 characters","register")
            is_valid= False
        if len(doctor['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if doctor['password'] != doctor['confirm']:
            flash("Passwords don't match","register")
        return is_valid

    @staticmethod
    def validate_login(doctor):
        is_valid = True
        query = "SELECT * FROM doctores WHERE email = %(email)s;"
        results = connectToMySQL(Doctor.db_name).query_db(query,doctor)
        if not EMAIL_REGEX.match(doctor['email']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if len(doctor['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        return is_valid   
