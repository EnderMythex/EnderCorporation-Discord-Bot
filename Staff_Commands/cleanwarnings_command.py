
# ------------------------------------------------ IMPORT / LIBRARY -------------------------------------------------

import discord
import json

# ------------------------------------------------ CONFIG / INTENT -------------------------------------------------

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

warnings = {}

# -------------------------------------------------- COMMAND ----------------------------------------------------------

async def cleanwarnings_command(interaction, user: discord.User):
    # Vérifie si l'ID de l'utilisateur est dans la liste des utilisateurs autorisés
    if str(interaction.user.id) not in config["authorized_users"]:
        await interaction.response.send_message("⚠ Vous n'êtes pas autorisé à exécuter cette commande.", ephemeral=True)
        return

    if user.id in warnings:
        warnings.pop(user.id)
        await interaction.response.send_message(f"📌 Les avertissements de {user.mention} ont été nettoyés.")
    else:
        await interaction.response.send_message(f"🔎 {user.mention} n'a pas d'avertissements.")