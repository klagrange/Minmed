# Set the path
import os
from flask_swagger import swagger
from flask import Flask, jsonify
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from application import create_app, db

app = create_app()

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Minmed profiling"
    swag['info']['description'] = "Simple user registration that will be categorized into a profile type depending on users' input"
    return jsonify(swag)

manager = Manager(app)
migrate = Migrate(app, db)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = os.getenv("IP", "0.0.0.0"),
    port = int(os.getenv("PORT", 5000)))
)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()