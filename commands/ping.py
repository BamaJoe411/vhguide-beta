@bot.slash_command(name="hify", guild_ids=[759605199634432020, 207346709209022465])
    @option("message", description="'H'ifys your message!")
    async def hify(ctx: discord.ApplicationContext, message: str):
        if ctx.channel_id == 937394251556356147 or ctx.channel_id == 923430896487506002:
            new_message = message.replace("h", "***h***").replace("H", "***H***")
            await ctx.respond(f"{new_message}")
        else:
            await ctx.respond("You cant use this command here. must be in channel <#923430896487506002>", ephemeral=True)