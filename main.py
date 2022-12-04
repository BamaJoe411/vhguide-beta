import discord
from discord import option
import os
from dotenv import load_dotenv


def main():

    load_dotenv()
    bot = discord.Bot()

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready and online!")

    @bot.slash_command(name="hify", guild_ids=[759605199634432020, 935128289821982770])
    @option("message", description="'H'ifys your message!")
    async def hify(ctx: discord.ApplicationContext, message: str):
        if ctx.channel_id == 937394251556356147 or ctx.channel_id == 923430896487506002:
            new_message = message.replace("h", "***h***").replace("H", "***H***")
            await ctx.respond(f"{new_message}")
        else:
            await ctx.respond("You cant use this command here. must be in channel <#937394251556356147>", ephemeral=True)

    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
