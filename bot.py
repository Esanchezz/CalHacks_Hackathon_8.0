# Discord bot for untilting

import discord
import json
import asyncio


client = discord.Client()
finalmessage  = ""
gamecount = 0


token = 'OTAxNjI2MDUyMTg5NzY1Njcz.YXSmsg.OCoEty6qu3QGZiY4x2fMDPS--Uw'
YOURGUILDSID = 
YOURID = 
YOURFILENAME = "untilt.json"

m = {}


@client.event
async def on_ready():
    print('Session started for {0.user}'.format(client))

@client.event
async def on_ready():
    global m

    with open(YOURFILENAME, "r") as j:
        m = json.load(j)
        j.close()

    if len(m) == 0:
        m = {}
        for member in client.get_guild(YOURGUILDSID).members:
            m[str(member.id)] = {"xp" : 0, "messageCountdown" : 0}

    print('ready')

    while True:
        try:
            for member in client.get_guild(YOURGUILDSID).members:
                m[str(member.id)]['messageCountdown'] -= 1
        except:
            pass
        await asyncio.sleep(1)


@client.event
async def on_message(message):
    global m
    global finalmessage

    if message.content.lower() ==  "!stopsession" and message.author.id == YOURID:
        with open(YOURFILENAME,'w') as j:
            j.write( json.dumps(m) )
            j.close()
        await message.channel.send('session stopped')
        await client.close()

    if message.content.lower() == "!minusgame":
        m[str(message.author.id)["xp"]] -= 1
        await message.channel.send("game subtracted")

    elif message.content == "!gplayed":
        await message.channel.send(str(m[str(message.author.id)]['xp']) + 'games')

    elif message.content == "!gstreak": #number of games won/lost in a streak



    

@client.event        
async def win_loss_ratio(W,L): #I'm tryimng to do the win/loss ratio im sorry im so bad pls dont make fun of me i am trying
    countW = 0
    countL = 0

    input('How was your game? Enter W or L: ')
    if input(W):
        countW += 1
    elif input(L):
        countL += 1
        return (countW,countL)
    elif countL % 3 == 0:
        print ("Hey, why not take a break? We noticed you lost a couple of games, but it's not the end of the world. You wouldn't like it if other players took their frustration out on you, so don't take it out on them. Come and relax for a bit.")
        return
         

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'bot-stuff':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower()  == 'bye':
            await message.channel.send(f'See you later {username}!')
            return


    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return

client.run(token)
