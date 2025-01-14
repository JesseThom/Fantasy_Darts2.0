from flask_app import app
from flask_app.controllers import controller_routes, controller_users,controller_teams,controller_players,controller_pools

if __name__ == "__main__":
    app.run(debug=True)