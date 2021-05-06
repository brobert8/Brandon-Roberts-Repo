import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Logged on as {0}!')

@client.event
async def on_member_join(member):
    print(f'{member} is a stupid stupid')

@client.event
async def on_member_remove(member):
    print('haha byeybe stinky')

#joseph
memberId = client.get_user(272820867162046464)
#UwU chat
channelId = client.get_channel(716923182145339453)
#cardo chat
formerChannel = client.get_channel(807440487937081384)
#general chat
@client.event()
async def on_voice_state_update(memberId ,formerChannel,channelId):
    chatId = client.get_channel(272820867162046464)
    await chatId.send('pp')

@client.command()
async def clear(ctx, amount=5):
    if amount > 10:
        await ctx.send('no more than 10 dickwad')
    else:
        await ctx.channel.purge(limit = amount)

@client.command()
async def helpMe(ctx):
    await ctx.send('Options are: \n .clear (amt) \n .ping \n .coinFlip \n .mikeGay')


@client.command()
async def ping(ctx):
    await ctx.send('pong')

@client.command()
async def join(ctx):
    channel = client.get_channel(807440487937081384)
    await ctx.connect()

# #joseph
# memberId = client.get_user(178581412604018689)
# #UwU chat
# channelId = client.get_channel(716923182145339453)
# #cardo chat
# formerChannel = client.get_channel(807440487937081384)
# #general chat
# @client.command()
# async def on_voice_state_update(memberId ,formerChannel,channelId):
#     chatId = client.get_channel(272820867162046464)
#     await chatId.send('pp')



@client.command()
async def coinFlip(ctx):
    responses = ['heads', 'tails']
    await ctx.send(f'{random.choice(responses)}')

#@client.command(aliases=['mike'])
#async def mikeGay(ctx):
 #   responses = ['yes','yes','very musch so','no', 'GAY GAY GAY','gay gay', 'god yes', 'fucks sake yes']
  #  await ctx.send(f'{random.choice(responses)}')


# @client.command()
# async def mikeQuotes(ctx):
#     responses = ['crazy how little i care about the people i went to high school with lmao', 'biggest adversary is my own mind',
#     'the replies have me sick to my stomach, bunch of casuals who don’t know shit about basketball',
#     'well it’s now official, fuck the suns',
#     'please go get fucking somebody this is so frustrating',
#     'literally what the fuck',
#     'GOOD START VALLEY BOYZ',
#     'i used to be so motivated what the fuck happened',
#     'can’t tell if twitter washed or I am',
#     'where is your mother',
#     '2020 bout to be a dope ass documentary',
#     'if i began podcasting about the suns who would listen?']
#     await ctx.send(f'{random.choice(responses)}')



client.run('NzA5MjE5OTEyMjI0MjExMDY1.XrnY5A.FbpLApPz5TaKmz0hCILxXApDVRo')
