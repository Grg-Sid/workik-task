import os
import discord.ext.commands as commands
from utils.db_manager import ServerAuthDBManager, UserAuthDBManager


server_auth_db = ServerAuthDBManager()
user_auth_db = UserAuthDBManager()


class Auth(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog is ready")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def authenticate_server(self, ctx):
        if server_auth_db.insert(ctx.guild.id):
            await ctx.send(f"Server {ctx.guild.name} is authenticated")
        else:
            await ctx.send(f"Server {ctx.guild.name} is already authenticated")

    @authenticate_server.error
    async def authenticate_server_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            msg = f"You're an average joe {ctx.message.author.mention}"
        await ctx.send(msg)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def authenticate_user(self, ctx):
        if user_auth_db.insert(ctx.author.id):
            await ctx.send(f"User {ctx.author.name} is authenticated")
        else:
            await ctx.send(f"User {ctx.author.name} is already authenticated")

    @authenticate_user.error
    async def authenticate_user_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            msg = f"You're an average joe {ctx.message.author.mention}"
        await ctx.send(msg)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def truncate_auth(self, ctx):
        server_auth_db.truncate()
        user_auth_db.truncate()
        await ctx.send("Authentication data truncated")

    @truncate_auth.error
    async def truncate_auth_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            msg = f"You're an average joe {ctx.message.author.mention}"
        await ctx.send(msg)


async def setup(client):
    server_auth_db.create_table()
    user_auth_db.create_table()
    await client.add_cog(Auth(client))
