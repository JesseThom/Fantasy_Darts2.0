from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Players_on_teams:
    def __init__(self,data:dict):
        #for every column in table from db, must have an attribute
        self.players_id = data['players_id']
        self.teams_id = data['teams_id']
        self.pools_id = data['pools_id']
#C
    @classmethod
    def create(cls,data):
        #1 query statement
        query = "INSERT INTO players_on_teams (players_id,teams_id,pools_id) VALUES (%(pid)s,%(tid)s,%(pool)s);"
        #2 contact the data
        team_id = connectToMySQL(DATABASE).query_db(query, data) 
        return team_id
# #R
    
    
#     @classmethod
#     def get_one_by_id(cls, data):
#         query = "SELECT * FROM teams WHERE id = %(id)s;"
#         results = connectToMySQL(DATABASE).query_db(query,data)
#         if not results:
#             return False
#         return cls(results[0])

#     @classmethod
#     def get_all(cls, data):
#         query = "SELECT * FROM teams WHERE pools_id = %(pools_id)s ORDER BY team_points DESC;"
#         results = connectToMySQL(DATABASE).query_db(query, data)
#         all_teams = []
#         for dict in results:
#             all_teams.append(cls(dict))
#         return all_teams
    
# #U
#     @classmethod
#     def update_one(cls,data):
#         query = "UPDATE teams SET team_points = %(team_points)s,team_update =%(team_update)s,enable = 0 WHERE id = %(id)s;"
#         return connectToMySQL(DATABASE).query_db(query,data)
    
#     @classmethod
#     def disable_all(cls):
#         query = "UPDATE teams SET team_update = 0, enable = 1;"
#         return connectToMySQL(DATABASE).query_db(query)
#D
    @classmethod
    def delete_one(cls,data):
        query = "DELETE FROM players_on_teams WHERE players_id= %(pid)s AND teams_id = %(tid)s AND pools_id = %(pool)s;"
        return connectToMySQL(DATABASE).query_db(query,data)