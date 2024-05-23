import discord
from discord.ext import commands
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment
load_dotenv()

# Get API key and Token
TOKEN = os.getenv("TOKEN")
API_KEY = os.getenv("GEMINI_API_KEY")

# Constants
PROJECT_URL = "https://github.com/scienmanas/JourneyGenie"
ERROR_MESSAGE = "An Unknown error occurred :("
FIRST_PROMPT = "You are an ai agent called Journey Genie. Chat with the person and undersatnd his needs. Your first reply should be something like this (not exactly, do add you touch): Hi, i am JourneyGenie 🧳, I am here to help you plan your trip 😊. You may ask where he want to go, What is his budget, his needs, his trip duration, his preferences, etc. Ask questions accordinly, and recommend him the best option. Also if further information is needed, then do that. Also keep the message less than 1900 characters"


class JourneyGenie(commands.Bot):

    def __init__(self) -> None:

        # Initialise the bot
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True

        super().__init__(intents=intents, command_prefix="&")

        # Initialise gemini models
        genai.configure(api_key=API_KEY)
        self.gemini = genai.GenerativeModel('gemini-1.5-pro-latest')
        self.genaration_config = genai.GenerationConfig(max_output_tokens=1500)

        # Chat-mode variables
        self.chat_mode = False

        # History varibale and safety variables
        self.history = []
        self.safety_settings = {
            "SEXUALLY_EXPLICIT": 'block_none'
        }  # This on;y works for received responses not for passed prompts. So don't pass harmful prompts

        # Configure chat
        self.chat = self.gemini.start_chat(history=self.history)

    async def on_ready(self) -> None:
        print("Logged in as: {0.user}".format(self))

    async def on_message(self, message: discord.Message) -> None:

        if message.author == self.user:
            return

        # Get the command
        message_received = message.content.lower()

        # Order of if-else is important here
        if message_received.startswith("&help"):
            await self.help(message=message)

        elif message_received.startswith("&stop_chat") and self.chat_mode is True:
            await self.stop_chat(message=message)

        elif message_received.startswith("&new_chat"):
            await self.new_chat(message=message)

        elif self.chat_mode is True:
            prompt = message_received
            await self.handle_chat(message=message, prompt=prompt)

        elif message_received.startswith("&start_chat") and self.chat_mode is False:
            await self.start_chat(message=message)

    @staticmethod
    async def help(message) -> None:

        embed = discord.Embed(
            title="JourneyGenie 🧳",
            description="Hey, want to get assisted with trip planning 🤔 ?",
            color=discord.Color.dark_purple()
        )

        embed.add_field(
            name="About",
            value="Hi, I am gen-ai trip planner bot, have a conversation with me and plan your next trip",
            inline=False
        )
        embed.add_field(
            name='Commands',
            value="To operate me, use **&<command name>**\n"
            "- **&help**: To view commands.\n"
            "- **&start_chat**: To start chatting.\n"
            "- **&new_chat**: To start a new chat\n"
            "- **Note**: When the chat mode is on, the bot will interact with every message send by user.",
            inline=False
        )

        embed.set_footer(
            text="This bot was developed by Manas"
        )

        await message.channel.send(embed=embed)

    async def start_chat(self, message) -> None:

        try:

            async with message.channel.typing():

                # start the chat
                self.chat_mode = True
                await message.channel.send("Chat Started !")

            async with message.channel.typing():

                if self.history is None or self.history == []:
                    response = self.chat.send_message(
                        FIRST_PROMPT, safety_settings=self.safety_settings)
                    text = response.text

                    self.history = self.chat.history
                    await self.send_message_to_user(message=message, text=text)

                else:
                    return

        except Exception as e:
            print(e)
            await message.channel.send(ERROR_MESSAGE)

    async def stop_chat(self, message) -> None:

        self.chat_mode = False
        await message.channel.send("Chat mode is disabled now")

    async def new_chat(self, message) -> None:

        try:

            async with message.channel.typing():

                # Delete history and reinstalize the chat
                self.history = []
                self.gemini.start_chat(history=self.history)

                # Set the chat-mode to false
                self.chat_mode = False

                await message.channel.send("New chat started !")

            async with message.channel.typing():

                response = self.chat.send_message(
                    FIRST_PROMPT, safety_settings=self.safety_settings)
                text = response.text

                self.history = self.chat.history
                await self.send_message_to_user(message=message, text=text)

        except Exception as e:

            print(e)
            await message.channel.send(ERROR_MESSAGE)

    async def handle_chat(self, prompt, message) -> None:

        try:

            async with message.channel.typing():

                response = self.chat.send_message(
                    prompt, safety_settings=self.safety_settings)
                text = response.text

                self.history = self.chat.history
                await self.send_message_to_user(message=message, text=text)

        except Exception as e:

            print(e)
            await message.channel.send(ERROR_MESSAGE)

    @staticmethod
    async def send_message_to_user(message, text) -> None:

        try:

            # Send the message
            await message.channel.send(text)

        except Exception as e:

            print(e)
            await message.channel.send(ERROR_MESSAGE)


def start_bot() -> None:
    journey_genie = JourneyGenie()
    journey_genie.run(token=TOKEN)


if __name__ == "__main__":
    start_bot()
