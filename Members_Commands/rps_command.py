
# ------------------------------------------------ IMPORT / LIBRARY -------------------------------------------------

import discord
import random

class RPSButtons(discord.ui.View):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.choice = None

# ------------------------------------------------ CONFIG / INTENT -------------------------------------------------

    @discord.ui.button(label="Pierre 🗿", style=discord.ButtonStyle.primary)
    async def pierre(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.user:
            return
        self.choice = "pierre"
        self.stop()

    @discord.ui.button(label="Feuille 🍀", style=discord.ButtonStyle.success)
    async def feuille(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.user:
            return
        self.choice = "feuille"
        self.stop()

    @discord.ui.button(label="Ciseaux ✂", style=discord.ButtonStyle.danger)
    async def ciseaux(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.user:
            return
        self.choice = "ciseaux"
        self.stop()

# -------------------------------------------------- COMMAND ----------------------------------------------------------

async def rps_command(interaction: discord.Interaction):
    view = RPSButtons(user=interaction.user)
    await interaction.response.send_message("Choisissez pierre 🗿, feuille 🍀 ou ciseaux ✂.", view=view)
    await view.wait()  

    if view.choice is None:
        await interaction.followup.send("Aucun choix effectué.")
        return

    choices = ["pierre", "feuille", "ciseaux"]
    bot_choice = random.choice(choices)
    user_choice = view.choice

    if user_choice == bot_choice:
        await interaction.followup.send(f"🎰 C'est une égalité. J'ai choisi {bot_choice}.")
    elif (user_choice == "pierre" and bot_choice == "ciseaux") or (user_choice == "feuille" and bot_choice == "pierre") or (user_choice == "ciseaux" and bot_choice == "feuille"):
        await interaction.followup.send(f"🎉 Vous avez gagné. J'ai choisi {bot_choice}.")
    else:
        await interaction.followup.send(f"💥 Vous avez perdu. J'ai choisi {bot_choice}.")