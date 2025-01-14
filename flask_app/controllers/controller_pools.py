from flask import render_template, redirect, session, request
from flask_app import app

from flask_app.models.model_pools import Pool
from flask_app.models.model_teams import Team
from flask_app.models.model_players import Player

#route to new pool form page
@app.route('/pool/new')
def pool_new():
    return render_template("pool_new.html")

#route to submit create pool form
@app.route('/pool/create',methods=["post"])
def pool_create():

    # data = {
    #     **request.form,
    #     'users_id':session['uuid']
    # }

    pool_id = Pool.create(request.form)

    if pool_id == False:
        print("Failed to create League")
    else:
        print(f"League Created at {pool_id} id")
    return redirect('/')

# route to enter pool by id
@app.route('/pool_login/<int:id>')
def pool_login(id):
    return redirect(f"/dashboard/{id}")

@app.route('/pool_delete/<int:id>')
def pool_delete(id):
    Pool.delete_one({'id':id})
    return redirect("/leagues")

# # route to show individual pool by uuid
# @app.route('/pool/<int:id>',methods=["post"])
# def pool_dashboard(id):
#     data = {
#         **request.form,
#         'id': id
#         }
    # team = Pool.get_one(data)
    # team_id = {'id':team.id}
    # players = Player.get_all_by_team(team_id)
    # return render_template("dashboard_old.html",)

# #route to show individual team by team id
# @app.route('/team/<int:id>')
# def team_show_by_id(id):
#     data = {'id': id}
#     team = Pool.get_one_by_id(data)
#     team_id = {'id':team.id}
#     players = Player.get_all_by_team(team_id)
#     return render_template("team_show.html", team=team,players=players)