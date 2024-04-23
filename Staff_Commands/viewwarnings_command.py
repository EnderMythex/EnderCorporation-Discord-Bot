import discord
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

warnings = {}

async def viewwarnings_command(interaction):
    # Vérifie si l'ID de l'utilisateur est dans la liste des utilisateurs autorisés
    if str(interaction.user.id) not in config["authorized_users"]:
        await interaction.response.send_message("⚠ Vous n'êtes pas autorisé à exécuter cette commande.", ephemeral=True)
        return

    embed = discord.Embed(title="❗ Avertissements de tout les membres", color=0xff0000)
    for user_id, user_warnings in warnings.items():
        user = await client.fetch_user(user_id)
        embed.add_field(name=user.name, value=', '.join(user_warnings), inline=False)
    await interaction.response.send_message(embed=embed)