import discord.ext.commands as commands


class Hello(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog is ready")

    @commands.command(aliases=["hi", "hello", "hlo"])
    async def hello_world(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}")


async def setup(client):
    await client.add_cog(Hello(client))
