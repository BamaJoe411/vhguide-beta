import discord
from discord import app_commands
import os
from dotenv import load_dotenv

MY_GUILD = discord.Object(id=207346709209022465)
MY_DEV = discord.Object(id=759605199634432020)


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        self.tree.copy_global_to(guild=MY_DEV)
        await self.tree.sync(guild=MY_GUILD)
        await self.tree.sync(guild=MY_DEV)


def main():
    load_dotenv()
    intents = discord.Intents.default()
    client = MyClient(intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user} (ID: {client.user.id})')

    @client.tree.command()
    @app_commands.describe(
        message='The message to be \'H\'ified'
    )
    async def hify(interaction: discord.Interaction, message: str):
        """'H'ifys your message!"""
        if interaction.channel_id == 937394251556356147 or interaction.channel_id == 923430896487506002:
            new_message = message.replace("h", "***h***").replace("H", "***H***")
            await interaction.response.send_message(f"{new_message}")
        else:
            error_msg = "You cant use this command here. must be in channel <#923430896487506002>"
            await interaction.response.send_message(error_msg, ephemeral=True)

    client.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
