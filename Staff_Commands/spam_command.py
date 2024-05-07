
# ------------------------------------------------ IMPORT / LIBRARY -------------------------------------------------

import discord
import json

# ------------------------------------------------ CONFIG / INTENT -------------------------------------------------

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# -------------------------------------------------- COMMAND ----------------------------------------------------------

async def spam_command(interaction, user: discord.User, message: str):
    # Vérifie si l'ID de l'utilisateur est dans la liste des utilisateurs autorisés
    if str(interaction.user.id) not in config["authorized_users"]:
        await interaction.response.send_message("⚠ Vous n'êtes pas autorisé à exécuter cette commande.", ephemeral=True)
        return

    for _ in range(5):  # Répète l'envoi du message 5 fois
        await user.send(message)
    await interaction.response.send_message(f"✅ Messages envoyés à {user.mention}.")