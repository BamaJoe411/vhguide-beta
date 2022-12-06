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
            error_msg = f"""
            I'm sorry to inform you, <@{interaction.user.id}>, but you are not allowed
            to use the `/hify` command here in <#{interaction.channel_id}>, because that
            would just be downright silly! Please head on over to <#923430896487506002>
            and use the command there as much as your heart desires.
            """
            await interaction.response.send_message(error_msg, ephemeral=True)

    @client.tree.command()
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        message='the message to send'
    )
    async def editmsg(interaction: discord.Interaction, message: str):
        """Edits a message"""
        if interaction.user.id == 196182776498749442:
            list_channel = client.get_channel(937394251556356147)
            list_message = await list_channel.fetch_message(1049762293585555589)
            await list_message.edit(content=message)
            await interaction.response.send_message("message should be edited", ephemeral=True)
        else:
            error_msg = f'Sorry, <@{interaction.user.id}> you are not <@196182776498749442>'
            await interaction.response.send_message(error_msg, ephemeral=True)

    @client.tree.command()
    @app_commands.checks.has_permissions(administrator=True)
    async def sendmsg(interaction: discord.Interaction):
        """sends a dummy message"""
        await interaction.response.send_message("this is a dummy message")

    client.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
