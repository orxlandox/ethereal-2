import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random


Client = discord.Client()
client = commands.Bot(command_prefix = ".")
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Loading Assets.'))
    time.sleep(1)
    await client.change_presence(game=discord.Game(name='Getting Information.'))
    time.sleep(1)
    await client.change_presence(game=discord.Game(name='Connecting to host.'))
    time.sleep(2)
    await client.change_presence(game=discord.Game(name='Loaded!'))
    time.sleep(1)
    await client.change_presence(game=discord.Game(name='Ethereal | My prefix is .'))

@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hey there cutie! Welcome to Ethereal! I hope you have an amazing time in our server!')
    print('Sent message to ' + member.name)

@client.event
async def on_message(message):
    if message.content.upper().startswith('.HELLO'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Hey there hoe." % (userID))
    if message.content.upper().startswith('!COIN'):
        variable = [
            'Tails',
            'Heads',]
        await client.send_message(message.channel, (random.choice(variable)))
    if message.content.upper().startswith('.QUOTE'):
        await client.send_message(message.channel, "A Quote Of The Day Has Not Yet Been Added.")
    if message.content.upper().startswith('.HELP'):
        embed = discord.Embed(title="Command List", colour=discord.Colour(0xc076aa), description="Here you will fing the command database for the ethereal bot!") 
        embed.set_author(name="Ethereal Command Database")
        embed.set_footer(text="Ethereal")
        embed.add_field(name="Command Prefix", value=".", inline=True)
        embed.add_field(name=".Hello", value="Say hey!", inline=False)
        embed.add_field(name=".Quote", value="Shows the quote of the day.", inline=False)
        embed.add_field(name=".Report ISSUE", value="Report and issue with the server, replace ISSUE with your actuall issue.", inline=True)
        embed.add_field(name=".Coin", value="Flips a coin.", inline=True)
        await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith('.LILY'):
        await client.send_message(message.channel, "Likes noodles, co-owner, ~~Weirdo~~, Oh yea yea yea is her favourite song so make sure to spam her DM's saying OH YEA YEA YEA")
    if message.content.upper().startswith('.COIN'):
        variable = [
            'Tails',
            'Heads',]
        await client.send_message(message.channel, (random.choice(variable)))
    if message.content.upper().startswith('.REPORT'):
        args = message.content.split(" ")
        await client.send_message(discord.Object(id='546702027783143431'), "%s" % (" ".join(args[1:])))
        embed = discord.Embed(title="Report Status", colour=discord.Colour(0xc076aa), description="View your report here.")
        embed.set_author(name="Ethereal Bot Reply")
        embed.set_footer(text="Ethereal")
        embed.add_field(name="Your report:", value="Submitted!", inline=True)
        await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith('.BEN'):
        await client.send_message(message.channel, "Likes noodles, owner, bod developer, ~~Hoe~~. Loves Billie Eilish. Doesnt give a shit about life.")


 
client.run("NTQ2MDEwMDI4MzczNDQyNTc4.D0h_zQ.oppFcZRxlTgHCD52dD80MTQdhUs")
