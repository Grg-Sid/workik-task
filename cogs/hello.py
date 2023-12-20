import discord.ext.commands as commands
import utils.utils as utils


class Hello(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog is ready")

    @commands.command(aliases=["hi", "hello", "hlo"])
    async def hello_world(self, ctx):
        if utils.user_authenticated(ctx.author.id) and utils.server_authenticated(
            ctx.guild.id
        ):
            await ctx.send(
                f"Hello {ctx.author.mention}, How are You? I am fine Thank You"
            )
        else:
            if not utils.server_authenticated(ctx.guild.id):
                if not utils.user_authenticated(ctx.author.id):
                    await ctx.send(
                        f"You're not authenticated {ctx.author.mention} and Server {ctx.guild.name} is not authenticated"
                    )
                else:
                    await ctx.send(f"Server {ctx.guild.name} is not authenticated")
            else:
                await ctx.send(f"You're not authenticated {ctx.author.mention}")


async def setup(client):
    await client.add_cog(Hello(client))
