import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def ping_command(interaction):
        latency = client.latency * 1000  # Convertit la latence en millisecondes
        await interaction.response.send_message(f"🏓 Pong! Latence : {latency:.0f}ms")