
# ------------------------------------------------ IMPORT / LIBRARY -------------------------------------------------

import discord
import datetime

# -------------------------------------------------- COMMAND ----------------------------------------------------------

async def time_command(interaction):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await interaction.response.send_message(f"🕑 L'heure actuelle est {current_time}.")