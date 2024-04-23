import discord

async def join_command(interaction: discord.Interaction):
        # Vérifie si l'utilisateur est dans un canal vocal
        if interaction.user.voice is None:
            await interaction.response.send_message("Vous devez être dans un canal vocal.")
            return
    
        channel = interaction.user.voice.channel
        await channel.connect()  # Fait rejoindre le bot au canal vocal
        await interaction.response.send_message(f"Connecté à {channel.name}.")