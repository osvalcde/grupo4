from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


class Consulta:
    db_name = "odonto"
    def __init__(self, data):
        self.id = data['id']
        self.fecha_hora = data['fecha_hora']
        self.comentario = data['comentario']
        self.pago_consulta = data['pago_consulta']
        self.pago_tratamiento = data['pago_tratamiento']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id_paciente = data['id_paciente']
        self.id_doctor = data['id_doctor']

    @classmethod
    def check(cls,data):
        query = "SELECT * FROM consultas WHERE id_paciente=%(id_paciente)s and id_doctor=%(id_doctor)s and fecha_hora=%(fecha_hora)s;"
        result=connectToMySQL(cls.db_name).query_db(query, data)
        if len(result) >= 1:
            return False
        return True
    
    @classmethod
    def agendar(cls,data):
        query = "insert into consultas (id_paciente, id_doctor, fecha_hora, created_at, updated_at) values(%(id_paciente)s ,%(id_doctor)s ,%(fecha_hora)s ,NOW() ,NOW();"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def desagendar(cls,data):
        query = "delete from consultas WHERE id_paciente=%(id_paciente)s and id_doctor=%(id_doctor)s and fecha_hora=%(fecha_hora)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_consulta(cls,data):
        query = "SELECT * FROM consultas WHERE id_paciente=%(id_paciente)s and id_doctor=%(id_doctor)s and fecha_hora=%(fecha_hora)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "select c.id, c.fecha_hora, c.comentario, c.pago_consulta, c.pago_tratamiento, c.created_at, c.updated_at, p.nombre as 'Paciente', d.nombre as 'Doctor' from consultas as c left join pacientes as p on c.id_paciente=p.id left join doctores as d on c.id_doctor=d.id"
        
        results = connectToMySQL(cls.db_name).query_db(query)
        consultas = []
        for consulta in results:
            consultas.append(cls(consulta))
        return consultas
    
    @classmethod
    def get_all_from_patient(cls,data):
        query = "select c.id, c.fecha_hora, c.comentario, c.pago_consulta, c.pago_tratamiento, c.created_at, c.updated_at, p.nombre as 'Paciente', d.nombre as 'Doctor' from consultas as c left join pacientes as p on id_paciente=p.id left join doctores as d on id_doctor=d.id where p.id=%(id)s"
        
        results = connectToMySQL(cls.db_name).query_db(query,data)
        consultas = []
        for consulta in results:
            consultas.append(cls(consulta))
        return consultas
    
    @classmethod
    def get_tratamientos(cls):
        query= "select * from tratamientos"
        results = connectToMySQL(cls.db_name).query_db(query)