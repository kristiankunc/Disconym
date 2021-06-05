import discord
import flask
from db_actions import Database
from aiohttp import web
from discord.ext import commands, tasks
from db_actions import Database
from flask import request, jsonify

app = flask.Flask(__name__)
routes = web.RouteTableDef()


def setup(bot):
    bot.add_cog(Webserver(bot))


class Webserver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.web_server.start()

        @app.route('/')
        def home():
            return '''<h1>Distant Reading Archive</h1>
                        <p>A prototype API for Disconym'''

        @app.route('/api/all', methods=['GET'])
        def api_all():
            total_stats = {"total messages": Database.get_total_messages(), "total servers": len(self.bot.guilds)}

            return jsonify(total_stats)

        @app.route('/api/msgs', methods=['GET'])
        def api_msgs():
            messages = Database.get_total_messages()

            return jsonify(messages)

        @app.route('/api/servers', methods=['GET'])
        def api_servers():
            servers = len(self.bot.guilds)

            return jsonify(servers)

        @app.errorhandler(404)
        def page_not_found(e):
            return "<h1>404</h1><p>The resource could not be found.</p>", 404

    @tasks.loop()
    async def web_server(self):
        app.run()

    @web_server.before_loop
    async def web_server_before_loop(self):
        await self.bot.wait_until_ready()