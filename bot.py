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
import youtube_dl
import datetime
import json
import asyncio

# ------------------------------------------------ CONFIG / INTENT -------------------------------------------------

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

guild_id = discord.Object(id=int(config["guild_id"]))

intents = discord.Intents.default()
intents.voice_states = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix=commands.when_mentioned_or('+'), help_command=None, intents=discord.Intents.all())

# ---------------------------------------------- NO PERMS NEED ------------------------------------------------------



from Members_Commands.test_command import test_command 

@client.tree.command(name="test", description="[NO PERMS NEEDED ✅] Testing command")
async def test_command_wrapper(interaction):
    await test_command(interaction) 



from Members_Commands.twitter_command import twitter_command

@client.tree.command(name="twitter", description="[NO PERMS NEEDED ✅] Search Twitter profiles by username")
async def twitter_command_wrapper(interaction, username: str): 
    await twitter_command(interaction, username)



from Members_Commands.version_command import version_command

@client.tree.command(name="version", description="[NO PERMS NEEDED ✅] Bot version")
async def version_command_wrapper(interaction):
    await version_command(interaction)



from Members_Commands.time_command import time_command

@client.tree.command(name="time", description="[NO PERMS NEEDED ✅] Affiche l'heure actuelle (Heure de france)")
async def time_command_wrapper(interaction):
    await time_command(interaction)



from Members_Commands.ping_command import ping_command

@client.tree.command(name="ping", description="[NO PERMS NEEDED ✅] Renvoie pong (Latence du bot)")
async def ping_command_wrapper(interaction):
    await ping_command(interaction)



from Members_Commands.join_command import join_command

@client.tree.command(name="join", description="[NO PERMS NEEDED ✅] Fait rejoindre le bot dans le canal vocal de l'utilisateur")
async def join_command_wrapper(interaction):
    await join_command(interaction)



from Members_Commands.listecouleurs_command import listecouleurs_command

@client.tree.command(name="listecouleurs", description="[NO PERMS NEEDED ✅] Affiche la liste des couleurs disponibles pour les embeds")
async def listecouleurs_command_wrapper(interaction):
    await listecouleurs_command(interaction)



from Members_Commands.rps_command import rps_command

@client.tree.command(name="rps", description="[NO PERMS NEEDED ✅] Joue à pierre, feuille, ciseaux avec le bot")
async def rps_command_wrapper(interaction: discord.Interaction):
    await rps_command(interaction)



from Members_Commands.hypixelplayer_command import hypixelplayer_command

@client.tree.command(name="hypixelplayer", description="[NO PERMS NEEDED ✅] Affiche les informations d'un joueur Hypixel")
async def hypixelplayer_command_wrapper(interaction: discord.Interaction, uuid: str): 
    await hypixelplayer_command(interaction, uuid) 





# --------------------------------------------- PERMS ADMIN NEEDED --------------------------------------------------

from Staff_Commands.listeuser_command import listeuser_command

@client.tree.command(name="listeuser", description="[ADMIN NEEDED ⛔] Listen role user")
async def listeuser_command_wrapper(interaction, role: discord.Role):  # Modifier le paramètre 'user' en 'role'
    await listeuser_command(interaction, role)  # Modifier l'argument passé à la fonction en 'role'




from Staff_Commands.love_command import love_command

@client.tree.command(name="love", description="[ADMIN NEEDED ⛔] Send a ❤ to a user")
async def love_command_wrapper(interaction, user: discord.User):
    await love_command(interaction, user)



from Staff_Commands.warn_command import warn_command

@client.tree.command(name="warn", description="[ADMIN NEEDED ⛔] Avertit un utilisateur")
async def warn_command_wrapper(interaction, user: discord.User, reason: str):
    await warn_command(interaction, user, reason)



from Staff_Commands.moveall_command import moveall_command

@client.tree.command(name="moveall", description="[ADMIN NEEDED ⛔] Déplace tous les membres en vocal dans un channel précis")
async def moveall_command_wrapper(interaction, channel: discord.VoiceChannel):
    await moveall_command(interaction, channel)



from Staff_Commands.viewwarnings_command import viewwarnings_command

@client.tree.command(name="viewwarnings", description="[ADMIN NEEDED ⛔] Voir tous les avertissements attribués aux personnes")
async def viewwarnings_command_wrapper(interaction):
    await viewwarnings_command(interaction)



from Staff_Commands.cleanwarnings_command import cleanwarnings_command

@client.tree.command(name="cleanwarnings", description="[ADMIN NEEDED ⛔] Nettoie les avertissements d'un utilisateur")
async def cleanwarnings_command_wrapper(interaction, user: discord.User):
    await cleanwarnings_command(interaction, user)



from Staff_Commands.say_command import say_command

@client.tree.command(name="say", description="[ADMIN NEEDED ⛔] Fait dire au bot ce que vous voulez")
async def say_command_wrapper(interaction, message: str):
    await say_command(interaction, message)



from Staff_Commands.saymp_command import saymp_command

@client.tree.command(name="saymp", description="[ADMIN NEEDED ⛔] Fait dire au bot ce que vous voulez en message privé")
async def saymp_command_wrapper(interaction, user: discord.User, message: str):
    await saymp_command(interaction,user, message)



from Staff_Commands.spam_command import spam_command

@client.tree.command(name="spam", description="[ADMIN NEEDED ⛔] Spam en mp")
async def spam_command_wrapper(interaction, user: discord.User, message: str):
    await spam_command(interaction,user, message)



from Staff_Commands.addroles_command import addroles_command

@client.tree.command(name="addroles", description="[ADMIN NEEDED ⛔] Ajoute un rôle à un membre précis")
async def addroles_command_wrapper(interaction, member: discord.Member, role: discord.Role):
    await addroles_command(interaction, member, role)



from Staff_Commands.ban_command import ban_command

@client.tree.command(name="ban", description="[ADMIN NEEDED ⛔] Ban a member")
async def ban_command_wrapper(interaction, member: discord.Member):
    await ban_command(interaction, member)



from Staff_Commands.kick_command import kick_command

@client.tree.command(name="kick", description="[ADMIN NEEDED ⛔] Kick a member")
async def kick_command_wrapper(interaction, member: discord.Member):
    await kick_command(interaction, member)



from Staff_Commands.createembed_command import createembed_command

@client.tree.command(name="createembed", description="[ADMIN NEEDED ⛔] Crée un embed avec couleur et image optionnelle")
async def createembed_command_wrapper(interaction: discord.Interaction, title: str, description: str, color: str, image_url: str = None):
    await createembed_command(interaction, title, description, color, image_url)





# ------------------------------------------------ MUSIC COMMAND (TEMP LOCATIONS) -------------------------------------------------

paused = False
pause_time = 0

# Assurez-vous d'avoir ces options pour youtube_dl
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
    'executable': config["ffmpeg_executable_path"]
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

# Modification de YTDLSource pour inclure plus d'informations
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('webpage_url')  # L'URL de la page YouTube
        self.duration = data.get('duration')  # La durée en secondes
        self.artist = data.get('uploader')  # L'artiste ou l'uploader

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=True):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

# Structure pour stocker les files d'attente par serveur
queues = {}

def check_queue(interaction):
    guild_id = interaction.guild.id
    if queues[guild_id]:
        voice_client = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)
        source = queues[guild_id].pop(0)
        voice_client.play(source, after=lambda x=None: check_queue(interaction))

# Ajout d'un message d'erreur si la vidéo ne peut pas être jouée
class MusicControlButtons(discord.ui.View):
    def __init__(self, interaction: discord.Interaction):
        super().__init__()
        self.interaction = interaction

    @discord.ui.button(label="Play", style=discord.ButtonStyle.primary, custom_id="play_button")
    async def play_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        global paused, pause_time
        vc = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)
        if vc and vc.is_connected():
            if paused:
                vc.play(vc.source, after=lambda e: print('done', e))
                vc.source = discord.PCMVolumeTransformer(vc.source)
                vc.source.volume = 0.5
                vc.source._position = pause_time
                paused = False
                # Création de l'embed
                embed = discord.Embed(title="✅ Succès", description="Musique relancée", color=0x00ff00)
                await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                # Création de l'embed
                embed = discord.Embed(title="⛔ Erreur", description="Aucune musique en pause", color=0xff0000)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            # Création de l'embed
            embed = discord.Embed(title="⛔ Erreur", description="Aucune musique en train de jouer", color=0xff0000)
            await interaction.response.send_message(embed=embed, ephemeral=True)


    @discord.ui.button(label="Pause", style=discord.ButtonStyle.primary, custom_id="pause_button")
    async def pause_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        global paused, pause_time
        vc = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)
        if vc and vc.is_connected() and vc.is_playing() and not paused:  # Ajoutez la condition not paused
            vc.pause()
            paused = True
            vc.source._position = pause_time  # Pas besoin d'appeler total_seconds()
            # Création de l'embed
            embed = discord.Embed(title="⏳ Pause", description="Musique en pause", color=0xFF7800)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            # Création de l'embed
            embed = discord.Embed(title="⛔ Erreur", description="Aucune musique en train de jouer ou déjà en pause", color=0xFF0000)
            await interaction.response.send_message(embed=embed, ephemeral=True)




    @discord.ui.button(label="Skip", style=discord.ButtonStyle.success, custom_id="skip_button")
    async def skip_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Création de l'embed
        embed = discord.Embed()

        # Vérifie si l'utilisateur est dans un canal vocal
        if interaction.user.voice is None:
            embed.add_field(name="⛔ Erreur", value="Vous devez être dans un canal vocal pour utiliser cette commande.", inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        # Récupère le client vocal du bot dans le serveur
        vc = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)

        if vc and vc.is_connected():
            # Vérifie si le bot est en train de jouer de la musique
            if vc.is_playing():
                vc.stop()  # Arrête la lecture actuelle
                embed.add_field(name="✅ Succès", value="Musique actuelle passée.", inline=False)
                embed.color = 0x00ff00  # Vert pour le succès
                await interaction.response.send_message(embed=embed)
            else:
                embed.add_field(name="⛔ Erreur", value="Aucune musique n'est actuellement jouée.", inline=False)
                embed.color = 0xff0000  # Rouge pour l'échec
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed.add_field(name="⛔ Erreur", value="Le bot n'est pas connecté à un canal vocal.", inline=False)
            embed.color = 0xff0000  # Rouge pour l'échec
            await interaction.response.send_message(embed=embed, ephemeral=True)
    
        # Supprime la vue après l'interaction
        self.stop()



@client.tree.command(name="play", description="[NO PERMS NEEDED ✅] Joue une vidéo YouTube dans le canal vocal ou l'ajoute à la file d'attente")
async def play_command(interaction: discord.Interaction, url: str):
    # Check if the user is in a voice channel
    if interaction.user.voice is None or interaction.user.voice.channel is None:
        embed = discord.Embed(title="⛔ Erreur", description="Vous devez être dans un canal vocal pour jouer une vidéo", color=0xFF0000)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    await interaction.response.defer()

    channel = interaction.user.voice.channel
    
    vc = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)
    if not vc or not vc.is_connected():
        vc = await channel.connect()
    
    # Crée la file d'attente pour le serveur si elle n'existe pas
    if interaction.guild.id not in queues:
        queues[interaction.guild.id] = []

    try:
        # Prépare la source audio
        player = await YTDLSource.from_url(url, loop=client.loop)
    except Exception as e:
        await interaction.followup.send(f"Erreur: Impossible de jouer la vidéo. Vérifiez l'URL ou réessayez. Erreur: {str(e)}")
        return
    
    # Si le bot est déjà en train de jouer de la musique, ajoute à la file d'attente
    if vc.is_playing() or queues[interaction.guild.id]:
        queues[interaction.guild.id].append(player)
        queue_embed = discord.Embed(title="🔂 File d'Attente", color=discord.Color.blue())
        for i, queued_song in enumerate(queues[interaction.guild.id], start=1):
            queue_embed.add_field(name=f"{i}. {queued_song.title}", value=f"Durée: {datetime.timedelta(seconds=player.duration)} \nArtiste: {queued_song.artist}", inline=False)
        await interaction.followup.send(f"{player.title} a été ajouté à la file d'attente.", embed=queue_embed)
    else:
        vc.play(player, after=lambda x=None: check_queue(interaction))
        now_playing_embed = discord.Embed(title="⏩ En train de jouer", description=f"[{player.title}]({player.url})", color=discord.Color.blue())
        now_playing_embed.add_field(name="Durée", value=str(datetime.timedelta(seconds=player.duration)))
        now_playing_embed.add_field(name="Artiste", value=player.artist)
        message = await interaction.followup.send(embed=now_playing_embed, view=MusicControlButtons(interaction))



# -------------------------------------------- SYNC  ----------------------------------------------------

@client.command()
async def sync(ctx):
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands!")
        await ctx.send(f"Synced {len(synced)} commands!")
    except Exception as e:
        print(e)

client.run(config["token"])
