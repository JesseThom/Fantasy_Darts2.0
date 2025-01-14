from flask import render_template, redirect, session, request, flash
from flask_app import app, JSON_FILE, MAXPLAYERS 
import json

from flask_app.models.model_players import Player #TODO import model file here
from flask_app.models.model_teams import Team
from flask_app.models.model_players_on_teams import Players_on_teams

@app.route('/player/update')
def player_update():
    if 'uuid' not in session:
        return redirect('/')
    
    # f = open('stats.json')
    # pythonanywhere location
    f = open(JSON_FILE)
    data = json.load(f)

    for i in data:
        player = Player.get_one(i)
        if not player:
            # print("-------------new player---------------")
            points = update_points(i)

            data = {
                **i,
                'player_points': points
            }
            Player.create(data)
        else:
            # print("-------------update player---------------")
            points = update_points(i)
            data= {
                **i,
                'id':player.id,
                'player_points': points
            }
            Player.update_one(data)

    update_team_points()
    return redirect('/leagues')

# route to add player to team
@app.route("/player/add/<int:pid>/<int:tid>/<int:pool>")
def player_add(pid,tid,pool):
    data = {
        'pid':pid,
        'tid':tid,
        'pool':pool
    }
    # # check if player is on already chosen
    temp = Player.verify(data)
    # print(temp)
    if temp == False:
        player = Player.get_one_by_id({"id":pid})
        # Player.add_player_to_team(data)
        Players_on_teams.create(data)
        flash(f"{player.first_name} {player.last_name} Added","err_taken")
    else:
        flash(f"{temp.first_name} {temp.last_name} is on another team, Choose again","err_taken")

    return redirect(f"/team/{tid}")

# route to remove player from team
@app.route("/player/remove/<int:pid>/<int:tid>/<int:pool>")
def player_remove(pid,tid,pool):
    data = {
        'pid':pid,
        'tid':tid,
        'pool':pool
    }
    Players_on_teams.delete_one(data)
    return redirect (f"/team/{tid}")

# update player points
def update_points(data):
    temp_points = 0
    temp_points = temp_points + (data['Whrse'] * 5)
    temp_points = temp_points + (data['Hat'] * 2.5)
    temp_points = temp_points + (data['HTon'] * 4.5)
    temp_points = temp_points + (data['LTon']* 1.5)
    temp_points = temp_points + (data['_9MR'] * 4.5)
    temp_points = temp_points + (data['_8MR'] * 4)
    temp_points = temp_points + (data['_7MR'] * 3.5)
    temp_points = temp_points + (data['_6MR'] * 3)
    temp_points = temp_points + (data['_5MR'] * 2)

    return temp_points

# update team points
def update_team_points():
    teams = Team.get_all()
    for team in teams:
        id = {'id': team.id}
        players = Player.get_all_by_team(id)
        temp_points = 0

        x=0
        for player in players:
            x = x+1
            
            # remove + 1 to add a non scoring sub
            if x == MAXPLAYERS + 1:
                break
            temp_points = player.player_points + temp_points

        team_points = team.team_points + temp_points
        data = {
            'id':team.id,
            'team_points': team_points,
            'team_update': temp_points
        }
        Team.update_one(data)

@app.route('/disable')
def disable():
    Team.disable_all()
    Player.reset_points()
    return redirect('/leagues')

#route to show individual player
@app.route('/player/<int:id>')
def player_show(id):
    data = {'id': id}
    player = Player.get_one_by_id(data)
    return render_template("player_show.html", player=player)