import discord
from discord import app_commands
from discord.ext import commands
import youtube_dl
import datetime
import random
import json
import asyncio
import aiohttp

async def fetch_hypixel_uuid(username, api_key):
    url = f"https://api.hypixel.net/find?key={api_key}&name={username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data['success']:
                    return data['player']['uuid']
                else:
                    return None
            else:
                return None

async def fetch_hypixel_player_data(uuid, api_key):
    url = f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

intents = discord.Intents.default()
client = discord.Client(intents=intents)



async def hypixelplayer_command(interaction: discord.Interaction, uuid: str):
        api_key = config["hypixel_api_key"]  # Assurez-vous que votre config.json contient votre clé API d'Hypixel
        player_data = await fetch_hypixel_player_data(uuid, api_key)
    
        if player_data and player_data.get("player"):
            player = player_data["player"]
            player_name = player.get("displayname", "Inconnu")
            first_login_timestamp = player.get("firstLogin", "Inconnu")
            last_login_timestamp = player.get("lastLogin", "Inconnu")
            lastLogout = player.get("lastLogout", "Inconnu")
            user_language = player.get("userLanguage", "Inconnu")
            newPackageRank = player.get("newPackageRank", "Inconnu")
            currentPet = player.get("currentPet", "Inconnu")
            mostRecentGameType = player.get("mostRecentGameType", "Inconnu")
            channel = player.get("channel", "Inconnu")
            uuid = player.get("uuid", "Inconnu")
            karma = player.get("karma", "Inconnu")

            # Convertit les timestamps en objets datetime
            first_login_datetime = datetime.datetime.fromtimestamp(int(first_login_timestamp) / 1000) if first_login_timestamp != "Inconnu" else "Inconnu"
            last_login_datetime = datetime.datetime.fromtimestamp(int(last_login_timestamp) / 1000) if last_login_timestamp != "Inconnu" else "Inconnu"
            lastLogout = datetime.datetime.fromtimestamp(int(lastLogout) / 1000) if lastLogout != "Inconnu" else "Inconnu"

            # Convertit les objets datetime en chaînes de caractères dans un format lisible
            first_login = first_login_datetime.strftime("%Y-%m-%d %H:%M:%S") if first_login_datetime != "Inconnu" else "Inconnu"
            last_login = last_login_datetime.strftime("%Y-%m-%d %H:%M:%S") if last_login_datetime != "Inconnu" else "Inconnu"
            lastLogout = lastLogout.strftime("%Y-%m-%d %H:%M:%S") if lastLogout != "Inconnu" else "Inconnu"
        
            # Crée un embed avec les informations du joueur
            embed = discord.Embed(title="◥◣  ◥◣  ◥◣   Informations du joueur   ◢◤  ◢◤  ◢◤", color=0xC913FF)
            embed.add_field(name="🪪 Name", value=f"```{player_name}```", inline=False)
            embed.add_field(name="📋 UUID", value=f"```{uuid}```", inline=False)

            embed.add_field(name="🎖️ Rang", value=f"```{newPackageRank}```", inline=True)
            embed.add_field(name="🌍 Language", value=f"```{user_language}```", inline=True)

            embed.add_field(name="🪄 Karma", value=f"```{karma}```", inline=False)

            embed.add_field(name="📆 First Login", value=f"```{first_login}```", inline=True)
            embed.add_field(name="📆 Last Login", value=f"```{last_login}```", inline=True)

            embed.add_field(name="📆 last Logout", value=f"```{lastLogout}```", inline=False)

            embed.add_field(name="🎮 Recent Game", value=f"```{mostRecentGameType}```", inline=True)
            embed.add_field(name="💬 Channel", value=f"```{channel}```", inline=True)
        
            embed.add_field(name="🧸 Current Pet", value=f"```{currentPet}```", inline=False)

            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            embed.set_footer(text=f"💾 {current_time} Hypixel DataBase Informations")
        
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Impossible de récupérer les informations du joueur. Vérifiez l'UUID ou réessayez plus tard.")