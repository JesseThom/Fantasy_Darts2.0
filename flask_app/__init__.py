from flask import Flask
from flask_bcrypt import Bcrypt
# from flask_socketio import SocketIO

app = Flask(__name__)
bcrypt = Bcrypt(app)
# socketio = SocketIO(app)

app.secret_key = 'its a secret to everybody'

# local database
DATABASE = "fantasy_darts_2.0"
# pythonanywhere database 
# DATABASE = "jessethommes$fantasy_darts_2"

# json file location
# local
JSON_FILE = 'stats.json'
# python anywhere
# JSON_FILE = '/home/jessethommes/Fantasy_Darts2.0/stats.json'

# max player per team
MAXPLAYERS = 4

LEAGUEMESSAGE = "6 Team Max, 4 player teams"