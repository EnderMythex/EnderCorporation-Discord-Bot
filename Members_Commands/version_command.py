import discord

async def version_command(interaction):
        testembed = discord.Embed(title="EnderCorporation Bot Version", description="⬆️ [BETA] V0.0.8",
                                  colour=discord.Colour.blurple())
        await interaction.response.send_message(embed=testembed, ephemeral=True)