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
    handler = logging.FileHandler(filename=discord.log, encoding='utf-8', mode='w')
    
    
    # Enable necessary intents
    intents = discord.Intends.default()
    intents.message_content = True
    intents.members = True

    # Get the bot token from environment variables
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        logger.error("DISCORD_TOKEN not found in environment variables.")
        exit(1)