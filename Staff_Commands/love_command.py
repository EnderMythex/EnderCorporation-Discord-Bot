import discord
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

async def love_command(interaction, user: discord.User):
    # Vérifie si l'ID de l'utilisateur est dans la liste des utilisateurs autorisés
    if str(interaction.user.id) not in config["authorized_users"]:
        await interaction.response.send_message("⚠ Vous n'êtes pas autorisé à exécuter cette commande.", ephemeral=True)
        return

    user1 = interaction.user
    await interaction.response.send_message(f"{user1.mention} a envoyé un ❤ à {user.mention}.")
    await user.send(f"Message de la part de {user1.mention} : ❤ ❤ ❤ ❤ ")