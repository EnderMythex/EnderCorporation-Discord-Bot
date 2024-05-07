
# ------------------------------------------------ IMPORT / LIBRARY -------------------------------------------------

import discord
import json

# ------------------------------------------------ CONFIG / INTENT -------------------------------------------------

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# -------------------------------------------------- COMMAND ----------------------------------------------------------

async def moveall_command(interaction, channel: discord.VoiceChannel):
    # Vérifie si l'ID de l'utilisateur est dans la liste des utilisateurs autorisés
    if str(interaction.user.id) not in config["authorized_users"]:
        await interaction.response.send_message("⚠ Vous n'êtes pas autorisé à exécuter cette commande.", ephemeral=True)
        return

    for member in interaction.guild.members:
        if member.voice and member.voice.channel != channel:
            await member.move_to(channel)
    await interaction.response.send_message(f"💨 Tous les membres ont été déplacés dans {channel.name}.")