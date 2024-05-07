
# ------------------------------------------------ IMPORT / LIBRARY -------------------------------------------------

import discord

# -------------------------------------------------- COMMAND ----------------------------------------------------------

async def version_command(interaction):
        testembed = discord.Embed(title="EnderCorporation Bot Version", description="⬆️ [BETA] V0.0.9",
                                  colour=discord.Colour.blurple())
        await interaction.response.send_message(embed=testembed, ephemeral=True)