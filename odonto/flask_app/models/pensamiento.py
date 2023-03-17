from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Pensamiento:
    db_name = 'pensamientos'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.descripcion = db_data['descripcion']
        self.idUsuario = db_data['idUsuario']
        self.created_at = db_data['created_at']
        self.updated_at=  db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO pensamientos (descripcion, idUsuario, created_at) VALUES (%(descripcion)s,%(idUsuario)s,%(created_at)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pensamientos;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_pensamientos = []
        for row in results:
            print(row['created_at'])
            all_pensamientos.append( cls(row) )
        return all_pensamientos
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM pensamientos WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE pensamientos SET descripcion=%(descripcion)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM pensamientos WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_pensamientos(pensamiento):
        is_valid = True
        if len(pensamiento['descripcion']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","pensamiento")
        if pensamiento['created_at'] == "":
            is_valid = False
            flash("Please enter a date","pensamiento")
        return is_valid

    @staticmethod
    def validate_pensamientos_updated(pensamiento):
        is_valid = True
        if len(pensamiento['descripcion']) < 1:
            is_valid = False
            flash("Description must be at least 3 characters","pensamiento")
        return is_valid
