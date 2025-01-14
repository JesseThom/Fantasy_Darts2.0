from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Pool:
    def __init__(self,data:dict):
        #for every column in table from db, must have an attribute
        self.id = data['id']
        self.pool_name = data['pool_name']
        self.bracket = data['bracket']

#C
    @classmethod
    def create(cls,data):
        #1 query statement
        query = "INSERT INTO pools (pool_name, bracket) VALUES (%(pool_name)s,%(bracket)s);"
        #2 contact the data
        pool_id = connectToMySQL(DATABASE).query_db(query, data) 
        return pool_id
#R
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM pools WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if not results:
            return False
        return cls(results[0])
    
    # @classmethod
    # def get_one_by_id(cls, data):
    #     query = "SELECT * FROM pools WHERE id = %(id)s;"
    #     results = connectToMySQL(DATABASE).query_db(query,data)
    #     if not results:
    #         return False
    #     return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pools;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_pools = []
        for dict in results:
            all_pools.append(cls(dict))
        return all_pools
#U
    @classmethod
    def update_one(cls,data):
        query = "UPDATE pools SET pool_name = %(pool_name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
#D
    @classmethod
    def delete_one(cls,data):
        query = "DELETE FROM pools WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)