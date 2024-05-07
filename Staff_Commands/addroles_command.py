
# ------------------------------------------------ IMPORT / LIBRARY -------------------------------------------------

import discord
import json

# ------------------------------------------------ CONFIG / INTENT -------------------------------------------------

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# -------------------------------------------------- COMMAND ----------------------------------------------------------

async def addroles_command(interaction, member: discord.Member, role: discord.Role):
    # Vérifie si l'ID de l'utilisateur est dans la liste des utilisateurs autorisés
    if str(interaction.user.id) not in config["authorized_users"]:
        await interaction.response.send_message("⚠ Vous n'êtes pas autorisé à exécuter cette commande.", ephemeral=True)
        return

    await member.add_roles(role)
    await interaction.response.send_message(f"Le rôle {role.name} a été ajouté à {member.display_name}.")