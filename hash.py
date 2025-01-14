from flask_app import app, bcrypt

print(bcrypt.generate_password_hash("whiskey"))