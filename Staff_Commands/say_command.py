import discord
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

async def say_command(interaction, message: str):
    # Vérifie si l'ID de l'utilisateur est dans la liste des utilisateurs autorisés
    if str(interaction.user.id) not in config["authorized_users"]:
        await interaction.response.send_message("⚠ Vous n'êtes pas autorisé à exécuter cette commande.", ephemeral=True)
        return

    await interaction.response.send_message(message)