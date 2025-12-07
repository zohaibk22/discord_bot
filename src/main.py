import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(filename="discord.log", encoding='utf-8', mode='w')
    
    
    # Enable necessary intents
    intents = discord.Intents .default()
    intents.message_content = True
    intents.members = True

    secret_role = "Admin"

    # Get the bot token from environment variables
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        logger.error("DISCORD_TOKEN not found in environment variables.")
        exit(1)

    bot = commands.Bot(command_prefix="*", intents=intents)

    @bot.event
    async def on_ready():
        print(f"We are ready to go in, {bot.user.name}")

    

    @bot.event
    async def on_member_join(member):
        logger.info(f"{member} has joined the server.")
        await member.send(f"Welcome to the server, {member.name}!")

    @bot.event
    async def on_message(message):
        logger.info(f"Message from {message.author}: {message.content}")
        # If out bot is the one writing the message, we dont want to reply
        if message.author == bot.user:
            return 
        
        if "shit" in message.content.lower():
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please don't use that word")

        await bot.process_commands(message)

    @bot.command()
    async def hello(ctx):
        await ctx.send(f"Hello, {ctx.author.mention}!")

    @bot.command()
    async def assign(ctx):
        role = discord.utils.get(ctx.guild.roles, name=secret_role)



    bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)

