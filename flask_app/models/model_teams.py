from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Team:
    def __init__(self,data:dict):
        #for every column in table from db, must have an attribute
        self.id = data['id']
        self.team_name = data['team_name']
        self.team_points = data['team_points']
        self.team_update = data['team_update']
        self.enable = data['enable']
        self.users_id = data['users_id']
        self.pools_id = data['pools_id']

#C
    @classmethod
    def create(cls,data):
        #1 query statement
        query = "INSERT INTO teams (team_name, pools_id, users_id) VALUES (%(team_name)s,%(pools_id)s,%(users_id)s);"
        #2 contact the data
        team_id = connectToMySQL(DATABASE).query_db(query, data) 
        return team_id
#R
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM teams WHERE users_id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if not results:
            return False
        return cls(results[0])
    
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM teams WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM teams;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_teams = []
        for dict in results:
            all_teams.append(cls(dict))
        return all_teams

    @classmethod
    def get_all_by_pool(cls, data):
        query = "SELECT * FROM teams WHERE pools_id = %(pools_id)s ORDER BY team_points DESC;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        all_teams = []
        for dict in results:
            all_teams.append(cls(dict))
        return all_teams
    
#U
    @classmethod
    def update_one(cls,data):
        query = "UPDATE teams SET team_points = %(team_points)s,team_update =%(team_update)s,enable = 0 WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def disable_all(cls):
        query = "UPDATE teams SET team_update = 0, enable = 1;"
        return connectToMySQL(DATABASE).query_db(query)
#D
    @classmethod
    def delete_one(cls,data):
        query = "DELETE FROM teams WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)