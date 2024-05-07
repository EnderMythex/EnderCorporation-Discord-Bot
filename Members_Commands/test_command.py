
# ------------------------------------------------ IMPORT / LIBRARY -------------------------------------------------

import discord
import datetime

# -------------------------------------------------- COMMAND ----------------------------------------------------------

async def test_command(interaction: discord.Interaction):
        testembed = discord.Embed(title="Test Message", description="👋 Hello, this is a test message!",
                                  colour=discord.Colour.blurple())
        await interaction.response.send_message(embed=testembed, ephemeral=True)
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCES  ] Message de test envoyée avec succès dans le serveur")