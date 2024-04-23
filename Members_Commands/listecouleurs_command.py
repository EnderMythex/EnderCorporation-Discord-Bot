import discord

async def listecouleurs_command(interaction: discord.Interaction):
        # Liste des couleurs disponibles
        colors = """
        - rouge
        - vert
        - bleu
        - jaune
        - violet
        - noir
        - orange
        """
        await interaction.response.send_message(f"🎨 Voici la liste des couleurs disponibles pour les embeds : ```{colors}```")