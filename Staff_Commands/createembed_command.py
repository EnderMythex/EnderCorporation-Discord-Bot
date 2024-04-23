import discord
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

async def createembed_command(interaction: discord.Interaction, title: str, description: str, color: str, image_url: str = None):
    # Vérifie si l'ID de l'utilisateur est dans la liste des utilisateurs autorisés
    if str(interaction.user.id) not in config["authorized_users"]:
        await interaction.response.send_message("⚠ Vous n'êtes pas autorisé à exécuter cette commande.", ephemeral=True)
        return

    # Dictionnaire des couleurs prises en charge
    colors = {
        "rouge": discord.Color.red(),
        "vert": discord.Color.green(),
        "bleu": discord.Color.blue(),
        "jaune": discord.Color.gold(),
        "violet": discord.Color.purple(),
        "noir": discord.Color.default(),
        "orange": discord.Color.orange(),
    }

    # Sélection de la couleur
    embed_color = colors.get(color.lower(), discord.Color.default())

    embed = discord.Embed(title=title, description=description, color=embed_color)

    # Ajoute l'image à l'embed si un URL d'image est fourni
    if image_url:
        embed.set_image(url=image_url)

    await interaction.response.send_message(embed=embed)