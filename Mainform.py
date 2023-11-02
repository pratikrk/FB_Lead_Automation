import discord
from discord.ext import commands
import requests
from webserver import keep_alive

import os

intents = discord.Intents.default()
intents.message_content = True  # Allow message content events

bot = commands.Bot(command_prefix='$', intents=intents)
TOKEN = "MTE1NzI4NzczMTkwMzM0MDU1NA.Gvn1Gd.sTd68bAhyQTJLOUJPkFOkhQgfpCoGh1ezexQy0"
FACEBOOK_USER_TOKEN = "EAAL1G9uiTYIBOZBXaVtFyXZAACbO4jIwW8DmxBFAXQjfq37hFHMOaX96ZBouedJ8BZA156KVJ2CZCyOJ1rgH4g05sd8yjY8ZAcrGCNyKi5DD1mAkohlTzvZBZAgpji32ZACTaOOnxzLOgRnu6d7j005RUkutYbFnmbt7svwvUAIPzjvOT6K2s0n02Lqlpafz1orAVCaUmMbcIT9ZBoTsCLEcHHQIz6s6MurL4fjUvkUNHbrUQZD"
PAGE_ID = "856779522306134"

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command()
async def get_fb_leads(ctx):
    url = f"https://graph.facebook.com/{PAGE_ID}/leads?access_token={FACEBOOK_USER_TOKEN}"
    response = requests.get(url)

    if response.status_code == 200:
        # Process and forward the leads to a Discord channel
        leads = response.json()
        for lead in leads['data']:
            full_name = ""
            email = ""
            created_time = lead.get('created_time', 'N/A')  # Default to 'N/A' if 'created_time' is not present

            # Check the values of specific attributes
            purpose_of_purchase = ""
            apartment_type = ""
            
            for field in lead['field_data']:
                if field['name'] == 'full_name':
                    full_name = field['values'][0]
                elif field['name'] == 'phone_number':
                    phone_number = field['values'][0]
                elif field['name'] == 'which_type_of_apartment_are_you_interested_in?':
                    apartment_type = field['values'][0]
                elif field['name'] == 'purpose_of_purchase:':
                    purpose_of_purchase = field['values'][0]
                elif field['name'] == 'budget_range:':
                    budget_range = field['values'][0]
                elif field['name'] == 'when_are_you_planning_to_make_a_purchase?':
                    purchase_timing = field['values'][0]

            # Check if the lead meets the filtering criteria
            if full_name and phone_number and created_time:
                await ctx.send(f"Name: {full_name}\nPhone Number: {phone_number}\nCreated Time: {created_time}\nApartment Type: {apartment_type}\nPurpose of Purchase: {purpose_of_purchase}\nBudget Range: {budget_range}\nPurchase Timing: {purchase_timing}")
                await ctx.send("________________________________")
            else:
                await ctx.send("Lead does not meet the filtering criteria.")
    else:
        await ctx.send("Failed to retrieve Facebook leads.")


keep_alive()
bot.run(TOKEN)
