import flask
from db_actions import Database
from discord.ext import ipc
from flask import jsonify

app = flask.Flask(__name__)
ipc_client = ipc.Client(secret_key = "Disconym")

@app.route('/')
def home():
    return '''<h1>Distant Reading Archive</h1>
            <p>A prototype API for Disconym'''

@app.route('/api/all', methods=['GET'])
def api_all():
    print(Database.read_api())
    total_stats = {"total messages": Database.read_api()[0], "total servers": Database.read_api()[1]}

    return jsonify(total_stats)

@app.route('/api/msgs', methods=['GET'])
def api_msgs():
    messages = Database.read_api()[0]

    return jsonify(messages)

@app.route('/api/guilds', methods=['GET'])
def api_guilds():
    member_count = Database.read_api()[1]
    
    return jsonify(member_count)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
	app.run(debug=True)