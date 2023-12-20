import os
import asyncio
import discord
from discord.ext import commands

TOKEN = os.environ.get(
    "TOKEN", "MTE4NDk0MzkzMzg4OTk4MjU5Ng.Gspuyf.cB7gnLbdr4SrFPCybzXZVWDtITbomJr5h8FgR4"
)

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot is ready")


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded {filename[:-3]} cog")


async def main():
    async with client:
        await load()
        await client.start(TOKEN)


asyncio.run(main())
