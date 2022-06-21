from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * "
        query += "FROM dojos "
        query += "WHERE name=%(name)s;"
        
        result = connectToMySQL(DATABASE).query_db(query, data)
        
        if len(result) > 0:
            return cls(result[0])
        else:
            return None
        
        
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * "
        query += "FROM dojos; "
        
        result = connectToMySQL(DATABASE).query_db(query)
        list_dojos = []
        
        for row in result:
            list_dojos.append(cls(row))
            
        if len(result) > 0:
            return list_dojos
        else:
            return None
        
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos( name, id, created_at, updated_at) "
        query += "VALUES(%(name)s, %(id)s, %(created_at)s, %(updated_at)s);"
        
        new_dojo = connectToMySQL(DATABASE).query_db(query, data)
        
    @classmethod
    def get_dojo_by_id(cls, data):
        query = "SELECT * "
        query += "FROM dojos "
        query += "WHERE id = %(id)s;"
        
        result = connectToMySQL(DATABASE).query_db(query, data)
        
        return result