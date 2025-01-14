from flask import render_template,redirect, session
from flask_app import app, LEAGUEMESSAGE

from flask_app.models.model_users import User
from flask_app.models.model_teams import Team
from flask_app.models.model_players import Player
from flask_app.models.model_pools import Pool

#landing page
@app.route('/')
def landing_page():
    if 'uuid' in session:
        return redirect('/leagues')
    
    return render_template("index.html")

@app.route('/dashboard/<int:id>')
def dashboard(id):
    pool = Pool.get_one({'id':id})
    teams = Team.get_all_by_pool({'pools_id': id})
    team_view = 0
    for team in teams:
        if team.users_id == session['uuid']:
            team_view = 1
            return render_template("dashboard.html",teams=teams,team_view=team_view,pool_id=id,pool=pool,msg=LEAGUEMESSAGE)
        else:
            team_view = 0
    return render_template("dashboard.html",teams=teams,team_view=team_view,pool_id=id,pool=pool,msg=LEAGUEMESSAGE)

@app.route('/leagues')
def leagues():
    if 'uuid' not in session:
        return redirect('/')
    
    pools = Pool.get_all()
    
    return render_template("leagues.html",pools=pools)

@app.route('/brackets/<int:id>')
def brackets(id):
    if 'uuid' not in session:
        return redirect('/')
    pool = Pool.get_one({'id':id})
    
    return render_template("brackets.html",pool=pool)

@app.route('/scoring')
def scoring():
    if 'uuid' not in session:
        return redirect('/')
    
    return render_template("scoring.html")

# @app.route('/player_list')
# def player_list():
#     if 'uuid' not in session:
#         return redirect('/')
    
#     players = Player.get_all()
#     user_id = {'id':session['uuid']}
#     team = Team.get_one(user_id)
#     if not team:
#         data= {'id':0}
#         count = {'player_count':5}
#     else:
#         data = {'id':team.id} 
#         count = Player.count_players(data)
#         if team.enable == 1:
#             count = {'player_count':5}
#     return render_template("player_list.html",players=players,count=count)

@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")