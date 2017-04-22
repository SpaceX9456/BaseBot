import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print(" ____                 ____        _    \n"
          "| __ )  __ _ ___  ___| __ )  ___ | |_  \n"
          "|  _ \ / _` / __|/ _ \  _ \ / _ \| __| \n"
          "| |_) | (_| \__ \  __/ |_) | (_) | |_  \n"
          "|____/ \__,_|___/\___|____/ \___/ \__|")
    print("--------------------------------------------------")
    print("Thanks for using My bot")
    print("--------------------------------------------------")
    print("Logged in as")
    print(client.user.name)
    print("\nMy Client ID")
    print(client.user.id)
    print("--------------------------------------------------")
    prefix = open('prefix.file').read()
    print("Prefix:")
    print(prefix)
    print("--------------------------------------------------")

@client.event
async def on_message(message):
    prefix = open('prefix.file').read()
    if message.content.startswith(prefix + 'messages'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith(prefix + 'ping'):
        temp = await client.send_message(message.channel, 'Pinging')
        await asyncio.sleep(2)
        await client.edit_message(temp, ':ping_pong: , Pong')


    elif message.content.startswith(prefix + 'help'):
        if message.author.id not in open('owner.file').read():
            await client.send_message(message.author, "The prefix is " + prefix + " and the commands are: \n \n"
                                "messages --> Shows the ammount of messages sent in the channel\n\n"
                                "ping --> Pings the bot\n\n"
                                "help --> Shows you this command")
        else:
            await client.send_message(message.author, "Hello Owner, The prefix is " + prefix + " and the commands are: \n\n"
                                "```messages --> Shows the ammount of messages sent in the channel\n\n"
                                "ping --> Pings the bot\n\n"
                                "help --> Shows you this command\n\n"
                                "setgame --> Sets the bot's game```")

    elif message.content.startswith(prefix + "invite"):
        await client.send_message(message.channel, "You can invite me here: https://discordapp.com/oauth2/authorize?client_id=" + client.user.id + "=bot&permissions=8")

    elif message.content.startswith(prefix + "info"):
        await client.send_message(message.channel, "```Hello I am a Discord bot that is programmed by SpaceX#0276 that is easy to host yourself.\n"
        "You can go to this link and just dowlowand it, from there follow the instructions, very simple.\n"
        "The person hosting owns the bot and the owner is free to edit anything he pleases.\n"
        "If you need any support with the bot you can go to this link https://discord.gg/SAERSza```")    

token = open('token.file').read()
client.run(token)
