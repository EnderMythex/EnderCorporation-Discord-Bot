import discord
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

warnings = {}

async def warn_command(interaction, user: discord.User, reason: str):
    # Vérifier si l'utilisateur est autorisé
    if str(interaction.user.id) not in config["authorized_users"]:
        await interaction.response.send_message("⚠ Vous n'avez pas la permission de faire ça !", ephemeral=True)
        return

    # Logique de la commande après vérification de l'autorisation
    if user.id not in warnings:
        warnings[user.id] = []
    warnings[user.id].append(reason)
    await user.send(f"🔑 Vous avez été averti pour la raison suivante : {reason}.")
    await interaction.response.send_message(f"🔑 {user.mention} a été averti pour la raison suivante : {reason}.")