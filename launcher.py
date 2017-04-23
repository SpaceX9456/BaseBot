
import os
import sys
import time
import logging
import tempfile
import traceback
import subprocess
from time import gmtime, strftime

setup = (open('setup.txt').read())
if setup == "no":
    print(" __        __   _ \n"
          " \ \      / /__| | ___ ___  _ __ ___   ___  \n"
          "  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ \n "
          "   \ V  V /  __/ | (_| (_) | | | | | |  __/ \n"
          "    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|")
    print("--------------------------------------------------")
    print("Hello This is a base bot made by SpaceX#0276")
    print("If you need any support with this bot go to https://discord.gg/SAERSza")
    print("Now to get you started, you will need to input your token for your bot")
    print("To get your token, you need to go to https://discordapp.com/developers/applications/me and create a app, then once you have done that, you need to click create a bot user.")
    newtoken = input("PLease input your bot's token: \n")
    o = open('token.file', 'w')
    o.write(newtoken)
    print("--------------------------------------------------")
    print("Thank you, I have received your token")
    print("--------------------------------------------------")
    print("You will also need to set up a owner.")
    print("To do this you will need your ID.")
    print("To get your ID you need to go to your Discord settings and go to appearance and enable developer mode.")
    newowner = input("Please input your User ID here: \n")
    o = open('owner.file', 'w')
    o.write(newowner)
    print("--------------------------------------------------")
    print("Thank you, I have received your ID.")
    print("--------------------------------------------------")
    print("Now we must set up a prefix. To do this, I am going to ask you what you want it to be, just putit in.")
    newprefix = input("Please input your prefix here: \n")
    o = open('prefix.file', 'w')
    o.write(newprefix)
    print("--------------------------------------------------")
    print("Thank you, I have received your prefix.")
    print("--------------------------------------------------")
    o = open('setup.txt', 'w')
    o.write("yes")
else:
    print(" __        __   _ \n"
          " \ \      / /__| | ___ ___  _ __ ___   ___  \n"
          "  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ \n "
          "   \ V  V /  __/ | (_| (_) | | | | | |  __/ \n"
          "    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|")
    print("--------------------------------------------------")
    print("Welcome to my base bot. This bot is simple to use and I hope you enjoy using it.")
    print("If you need support go to https://discord.gg/SAERSza and we will be happy to help you.")
    print("You may also join the server above to get updates for when the bot gets updated and new features arise!")
    print("--------------------------------------------------")

print("Here you will have some options to chose from, just type in a option to get started!")
print("--------------------------------------------------")
option = input("What would you like to do right now. \n"
               "\n"
               "1) Start the bot \n"
               "\n"
               "2) Reset the bot's token \n"
               "\n"
               "3) Update the owner \n"
               "\n"
               "4) Exit the launcher \n")
print("--------------------------------------------------")
if option == "1":
    interpreter = sys.executable
    cmd = (interpreter, "BaseBot.py")

    while True:
        try:
            code = subprocess.call(cmd)
        except KeyboardInterrupt:
            break

elif option == "2":
    print("--------------------------------------------------")
    changetoken = input("Please input your new bot token: \n")
    o = open('token.file', 'a')
    o.write(changetoken)
    print("Thank you, I have received your new token")
    print("You will now be directed to the menu")
    print("--------------------------------------------------")
    newoption = input("What would you like to do right now. \n"
                   "\n"
                   "1) Start the bot \n"
                   "\n"
                   "2) Exit the launcher \n")
    print("--------------------------------------------------")
    if option == "1":
        interpreter = sys.executable
        cmd = (interpreter, "BaseBot.py")

        while True:
            try:
                code = subprocess.call(cmd)
            except KeyboardInterrupt:
                break

    elif option == "2":
        print("Thank you for using my bot, enjoy your day!")
        print("You may get a error when exiting this, ignore it.")
        exit()
    else:
        print("Well you must provide a answer!")

elif option == "3":

        print("--------------------------------------------------")
        changeowner = input("Please input your new owner ID: \n")
        o = open('owner.file', 'a')
        o.write(changeowner)
        print("Thank you, I have received your new token")
        print("You will now be directed to the menu")
        print("--------------------------------------------------")
        newoption = input("What would you like to do right now? \n"
                       "\n"
                       "1) Start the bot \n"
                       "\n"
                       "2) Exit the launcher \n")
        print("--------------------------------------------------")
        if option == "1":
            interpreter = sys.executable
            cmd = (interpreter, "BaseBot.py")

            while True:
                try:
                    code = subprocess.call(cmd)
                except KeyboardInterrupt:
                    break

        elif option == "2":
            print("Thank you for using my bot, enjoy your day!")
            print("You may get a error when exiting this, ignore it.")
            exit()
        else:
            print("Well, you must provide a answer!")

elif option == "4":
    print("Thank you for using my bot, enjoy your day!")
    print("You may get a error when exiting this, ignore it.")
    exit()
else:
    print("Well, you must provide a answer!")
