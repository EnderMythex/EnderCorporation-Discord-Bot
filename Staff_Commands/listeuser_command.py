
# ------------------------------------------------ IMPORT / LIBRARY -------------------------------------------------

import discord
import json

# ------------------------------------------------ CONFIG / INTENT -------------------------------------------------

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# -------------------------------------------------- COMMAND ----------------------------------------------------------

async def listeuser_command(interaction, role: discord.Role):
    if str(interaction.user.id) not in config["authorized_users"]:
        await interaction.response.send_message("⚠ Vous n'êtes pas autorisé à exécuter cette commande.", ephemeral=True)
        return

    members_with_role = [member for member in role.members]
    member_name = [member.name for member in members_with_role]
    
    await interaction.response.send_message(f"Membres avec le rôle {role.name} : ``` \n{'\n'.join(member_name)} ``` ")
