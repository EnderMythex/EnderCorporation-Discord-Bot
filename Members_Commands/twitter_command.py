
# ------------------------------------------------ IMPORT / LIBRARY -------------------------------------------------

import discord
import tweepy
import json

# -------------------------------------------------- COMMAND ----------------------------------------------------------

# Chargez les clés d'API à partir du fichier de configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    API_KEY = config["twitter_api_key"]
    API_SECRET_KEY = config["twitter_api_secret_key"]

def utilisateur_existe(username: str):
    # Implémentation de la logique pour vérifier si l'utilisateur existe
    # Exemple de logique simple : vérifier si la longueur du nom d'utilisateur est supérieure à 3
    if len(username) > 3:
        return True
    else:
        return False

async def recherche_utilisateur_twitter(username: str):
    # Vérifie si l'utilisateur existe avant de donner le lien
    if utilisateur_existe(username):
        return f"Voici le profil Twitter de l'utilisateur X : https://x.com/{username}"
    else:
        return "Utilisateur X (Twitter) non trouvé"

async def twitter_command(interaction, username: str):
    # Exemple de recherche d'utilisateur Twitter fictive
    user = await recherche_utilisateur_twitter(username)  # Ajoute 'await' ici
    
    if user:
        await interaction.response.send_message(user)
    else:
        await interaction.response.send_message("Utilisateur X (Twitter) non trouvé")