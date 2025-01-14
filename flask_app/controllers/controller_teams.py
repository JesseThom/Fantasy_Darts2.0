from flask import render_template, redirect, session, request
from flask_app import app, MAXPLAYERS

from flask_app.models.model_teams import Team
from flask_app.models.model_players import Player

#route to new team form page
@app.route('/team/new/<int:id>')
def team_new(id):
    return render_template("team_new.html",pool_id=id)

#route to submit create team form
@app.route('/team/create',methods=["post"])
def team_create():

    data = {
        **request.form,
        'users_id':session['uuid']
    }
    team_id = Team.create(data)

    if team_id == False:
        print("Failed to create team")
    else:
        print(f"team Created at {team_id} id")
    return redirect(f'/dashboard/{data["pools_id"]}')

#route to show individual team by team id
@app.route('/team/<int:id>')
def team_show_by_id(id):
    team = Team.get_one_by_id({'id':id})
    players = Player.get_all_by_team({'id':id})
    null_players = Player.get_all_by_pool({'id':team.pools_id})
    count = Player.count_players({'id':id})
    return render_template("team_show.html",team=team, players=players, null_players=null_players,count=count,max=MAXPLAYERS)