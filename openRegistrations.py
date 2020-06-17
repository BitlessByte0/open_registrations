#!/usr/bin/env python3

from discord_webhook import DiscordWebhook
from datetime import datetime
import json
import requests

now = datetime.now()

configData = []
webhookUrl = ""
quietTimeStart = 0
quietTimeEnd = 0
quitTime = False
checkMaintenance = False
sendClosedNotifications = False

def usage():
    print("./config.json Example:")
    print('''
{
    "webhookUrl" : "https://discord.com/api/webhooks/722538292381483045/DTYfCv4u9rNjWI_cBUj1HCiXoyGbqpHW5RdP-Ve47E-C_sIZEia8OmnAkT2fRnbghvOD",
    "quietTimeHours": { "start" : "23", "end" : "23" },
    "checkMaintenance": "1",
    "sendClosedNotifications": "1",
    "sites": [
        {
            "name": "drunkenSlug", "url":"https://drunkenslug.com/register", "search": "Sorry! The Bar is closed.", "open": "1"
        },
        {
            "name": "omgwtfnzbs", "url":"https://omgwtfnzbs.me/register", "search": "Public Registrations have been <font color=\"red\">disabled</font> by the site admin</b><br /><b>In order to register, you need at least a <u>valid invite code</u>", "open": "1"
        },
        {
            "name": "nzbplanet", "url":"https://nzbplanet.net/register", "search": "Registrations are currently invite only", "open": "1"
        }
    ]
}
    ''')
    exit(0)

def loadVariables():    
    try:
        webhookUrl = configData['webhookUrl']
    except:
        print("Error, the webhookUrl field is not correct in the config.json.") 
        usage()

    try:
        quietTimeStart = int(configData['quietTimeHours']['start'])
        quietTimeEnd = int(configData['quietTimeHours']['end'])
    except:
        print("Error, the quietTimeHours field is not correct in the config.json.")
        usage()

    try:
        checkMaintenance = int(configData['checkMaintenance'])
    except:
        print("Error, the checkMantenance field is not correct in the config.json.")
        usage()

    try:
        sendClosedNotifications = int(configData['sendClosedNotifications'])
    except:
        print("Error, the sendClosedNotifications field is not correct in the config file.")
        usage()

    return webhookUrl, quietTimeStart, quietTimeEnd, checkMaintenance, sendClosedNotifications

def calculateQuietTime():
    current_time = int(now.strftime("%H"))
    if quietTimeStart == quietTimeEnd:
        quitTime = False
    elif quietTimeStart < quietTimeEnd:
        if current_time >= quietTimeStart and current_time < quietTimeEnd:
            quitTime = True        
    else:
        if current_time >= quietTimeEnd or current_time < quietTimeStart:
            quitTime = True

# Open config file for reading
with open('./config.json') as json_file:
    configData = json.load(json_file)

# Check that config data from the file was obtained succesfully
if  len(configData) == 0:
    print("Error, no configuration data supplied. Please place a config.json file inside the same directory as this script.")
    usage()

# Load variables from the config data
webhookUrl, quietTimeStart, quietTimeEnd, checkMaintenance, sendClosedNotifications = loadVariables()    

# Calculate whether we are currently in quiet time
calculateQuietTime()

# Check if the site data was obtained succesfully from the config file
try:
    # Iterate through each of the given sites and check if they have open registrations
    for p in configData['sites']:
        print("--------------------")
        # Load site specific variables
        try:
            url = p['url']
            search = p['search']
            site = p['name']
            checkOpen = int(p['open'])
        except:
            print("Error, one of the sites field is not correct in the config.json.")
            print("Make sure that each site has a \"url\", '\"search\", \"site\" and \"open\" field.")
            usage()
        
        # Only proceed if user wants to check if this site is open
        if checkOpen:
            print("Checking " + site + " for open registration...")
            page = requests.get(url)
            pageText = page.text

            # If the search query is in the HTML then the site is closed
            if search in pageText:
                print("Registration is closed for " + site)
                # If it isn't quiet time and the user wants notifications of closed sites, send Discord message
                if not quitTime and sendClosedNotifications:
                    print("Sending Discord message...")
                    webhook = DiscordWebhook(url=webhookUrl, content='Registration is closed for ' + site)
                    response = webhook.execute()
            
            # If the search query is *NOT* in the HTML then presume the site is open
            elif search not in pageText:
                # Sometimes sites go down for maintenance causing a false positive
                # If user specifies, check if the HTML contains the word maintenance 
                #   ...before sending Discord message stating the site is open
                if checkMaintenance:
                    if "maintenance" in pageText:
                        print(site + "is down for maintenance.")
                        print("Sending Discord message...")
                        webhook = DiscordWebhook(url=webhookUrl, content=site + ' is down for maintenance!' + '\n' + url)
                        response = webhook.execute()
                    else:
                        print("Sending Discord message...")
                        print("Registration is open for " + site)
                        webhook = DiscordWebhook(url=webhookUrl, content='Registration is open for ' + site + '\n' + url)
                        response = webhook.execute()
                else:
                    print("Sending Discord message...")
                    print("Registration is open for " + site)
                    webhook = DiscordWebhook(url=webhookUrl, content='Registration is open for ' + site + '\n' + url)
                    response = webhook.execute()
        print("--------------------")
except KeyError:
    print("Error, the sites field is not correct in the config.json.")
    usage()