# -------------------------------------------- © EnderMytex Script Copyright ---------------------------------------------------
# -                                                                                                                            -
# -   Crédit : EnderMythex & Chat GPT-4                                                                                        -
# -                                                                                                                            -
# -   FR : Ce script nécessite une autorisations de la part de EnderMythex avant d'être modifié ou publié.                     -
# -   EN : This script requires authorization from EnderMythex before being modified or published.                             -
# -                                                                                                                            -
# ------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------ IMPORT / LIBRARY -------------------------------------------------

import discord
from discord import app_commands
from discord.ext import commands
from discord import Embed
import json
import datetime
import asyncio

# ------------------------------------------------ CONFIG / INTENT -------------------------------------------------

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

guild_id = discord.Object(id=int(config["guild_id"]))

intents = discord.Intents.default()
intents.voice_states = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix=commands.when_mentioned_or('+'), help_command=None, intents=discord.Intents.all())

# -------------------------------------------- ACTIVITY / RPC  ----------------------------------------------------

async def update_presence():
    while True:
        # Affiche "Joue à EnderComTY"
        game = discord.Game("🎮 EnderComTY")
        await client.change_presence(activity=game)
        await asyncio.sleep(3)  # Attend 3 secondes

        # Affiche l'heure locale
        local_time = datetime.datetime.now().strftime("%H:%M:%S")
        game = discord.Game(f"⏳ Heure locale: {local_time}")
        await client.change_presence(activity=game)
        await asyncio.sleep(3)  # Attend 3 secondes

        # Affiche l'heure locale
        game = discord.Game("💾 Version : V0.0.9")
        await client.change_presence(activity=game)
        await asyncio.sleep(3)  # Attend 3 secondes

# ------------------------------------------------ ONLINE MS ---------------------------------------------------------

@client.event
async def on_ready():
    client.loop.create_task(update_presence())
    channel = client.get_channel(1202292341646299236)  # Remplacez ID_DU_CANAL par l'ID réel du canal
    embed = discord.Embed(
        title='✅ Bot Online',
        description='[Version V0.0.9] <@1205192151881752636> is now online / All Commands is ready !\n \n 📌 Errors / Old Errors : \n - ~~AUTO ANSWER MP MESSAGES IN MAINTENANCE~~ (FIXED)',
        color=discord.Color.green()
    )
    await channel.send(embed=embed)

# --------------------------------------------------- MP MS -----------------------------------------------------------

users_last_message_time = {}

@client.event
async def on_message(message):
    # Vérifie si le message provient du bot lui-même
    if message.author == client.user:
        return  # Ignore les messages du bot lui-même

    # Vérifie si le message est un message privé (DM)
    if isinstance(message.channel, discord.DMChannel):
        user_id = message.author.id  # Obtient l'ID de l'utilisateur
        current_time = datetime.datetime.now()

        # Vérifie si l'utilisateur a déjà reçu un message
        if user_id in users_last_message_time:
            time_since_last_message = current_time - users_last_message_time[user_id]
            if time_since_last_message.total_seconds() < 10:
                # Si moins de 10 secondes se sont écoulées depuis le dernier message, ne fait rien
                return
        else:
            # Si l'utilisateur n'a pas encore reçu de message, enregistre le moment actuel
            users_last_message_time[user_id] = current_time

        # Prépare l'embed
        embed = discord.Embed(
            title='🔔 EnderComTY Notifications',
            description='Hi, Join this server : https://discord.gg/fz2Sr7rBcw',
            color=discord.Color.yellow()
        )
        # Envoie l'embed en réponse dans le DM de l'utilisateur
        await message.author.send(embed=embed)
        return
    
# --------------------------------------------------- NOTIF PING MS -----------------------------------------------------------

    # Vérifie si le message est envoyé dans un canal de serveur (guild)
    if isinstance(message.channel, discord.TextChannel):
        if message.channel.name == '⎝💫⎠free-ugc-roblox' or message.channel.name == '⎝👒⎠coming-free-ugc-roblox':
            role = discord.utils.get(message.guild.roles, name="Free UGC Limited Game")
            if role:
                if message.channel.name == '⎝💫⎠free-ugc-roblox':
                    title = "**NEW Free limited !**"
                else:
                    title = "**NEW Free limited is coming soon !**"

                embed = Embed(
                    title=title,
                    description="*To deactivate this ping click on the **button** \"Free UGC Limited Game\" in this channel : <#1069967789911195689>*",
                    color=0xFFD700  # Couleur dorée
                )
                embed.set_footer(text=f"Message envoyé dans le channel : {message.channel.name} du serveur : {message.guild.name}")
                await message.reply(role.mention, embed=embed)
                await message.add_reaction('👍')  # Ajoute l'emoji du pouce levé
                await message.add_reaction('❤')
                print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCES  ] Message envoyé dans le channel : {message.channel.name} du serveur : {message.guild.name}")
            else:
                await message.channel.send('Rôle non trouvé.')

client.run(config["token"])

