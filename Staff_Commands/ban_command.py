import discord
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

async def ban_command(interaction, member: discord.Member):
    # Vérifie si l'ID de l'utilisateur est dans la liste des utilisateurs autorisés
    if str(interaction.user.id) not in config["authorized_users"]:
        await interaction.response.send_message("⚠ Vous n'êtes pas autorisé à exécuter cette commande.", ephemeral=True)
        return

    await member.ban()
    await interaction.response.send_message(f"{member.display_name} a été banni.")