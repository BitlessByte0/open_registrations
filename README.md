## Description
***Note: It is recommended to run this script on a server using cron jobs***


This Python script is designed to check private websites to see if they currently have open registrations and then send a Discord message via a bot informing users of the website's current registration state. There will be one Discord message for each site that is set to be checked in the config file.

To do so, the script looks at the website's registration page and checks if it has a specific string which defines that it is closed. For example, if the phrasing "Open registrations are currently closed. You will need an invite code to join!" is found on the page, then the site is closed. However, if this phrase is not found on the website, the site is open. 

This method can return a false positive in two scenarios:
    1. The site owner has chosen to change the wording of their site
    2. The site is down for maintenance

The first false positive cannot be avoided, and users will have to update their settings in order to fix this false positive if it occurs.
The second false positive can be limited. To do so, the user can define a *check for maintenance* setting to be true or false. If set, the script will then check for the word "maintenance" in the site's HTML. If found, the script will send a Discord message saying the site is down for maintenance. If set, both "maintenance" and the user defined search query must *not* be found on the website for a Discord message to be sent stating that the site is open.
This setting has not been thoroughly tested, so ***use at your own risk***

The user has the option to set a quiet time for the script. During this time, there will be no Discord messages sent for *closed* registrations. *Open* registrations will ignore this quiet time and a Discord message will always be sent if a website is found to have *open* registration. 


***Note: Quiet time is set only by hours (no minutes or seconds) and it is in a 24hr format***
***Note: Quiet time is set in PST***


Quiet time can be used to fit the following scenario:
The user wants to only receive one notification per day if the site is closed. But, the user also wants to run the script once an hour to be immediately notified of open registrations. In this case, the user can set his quiet time from 01 until 24. When the script runs at 00 it will send a message stating the site is closed (granted that is the case). The 23 other times it runs that day, no Discord messages will be sent unless the site has open registrations.

The user has the option to configure sending alerts for closed registrations. If enabled, every time the script is ran a Discord message will be sent stating the current condition of registration for the website. If disabled, the script will only send a Discord message if the website's registration is *open*.

The user also has the option to enable/disable a specific site in their config file. This is done by setting the *open* field in the config file. If enabled, the site will be checked for open/closed registrations when the script is ran, otherwise, the script will ignore this site. This can be handy if the user succesfully registers for a site, but doesn't want to delete its information from the config file in case a friend needs them to check for open registrations in the future.

To ensure best results when setting up your config file, visit a site that currently has closed registrations. Find a defining piece of text on their site that says their registration is closed, and copy that into your config file. Some sites will inject HTML into these messages (an example of this is seen in the provided config file). In these cases, you will need to copy the HTML code for the message and not just the text. Using the link below, you can view the HTML code in Chrome and copy it from there (if you don't have Chrome, a quick search online will help you learn how to do it in your browser of choice).
Link: **https://www.lifewire.com/view-html-source-in-chrome-3466725**



## Settings
#### ***The only settings that will need changed are in config.json***
    webhookUrl: This is the webhook url for your Discord bot


    quietTimeHours: Quiet time disables Discord messages for closed registrations (open registrations ignore quitTimeHours and send a Discord message anyway)


        start**: This is the hour when quitTime will start (in PST)


        end: This is the hour when quitTime will end (in PST)


    checkMaintenance: Can be either a 1 or a 0. 1 enables check for maintenance and 0 disables it


    sendClosedNotifications: Can be either a 1 or a 0. 1 enables sending closed notifications and 0 disables it


    sites:

        name: The name of the site you want to search (only necessary for naming in Discord messages and can be left as a blank string)


        url: The url of the site you want to check (be sure that it is the registration part of the site. i.e. https://drunkenslug.com/***register***)


        search: This is the search string which will tell if the registration is open or closed (make sure it's a good one)


        open: Can be either a 1 or a 0. 1 enables checking this site and 0 disables it



## Obtaining a Discord Webhook Url
To get a Discord Webhook Url, you will need to be managing a Discord server. If you don't already have managerial access to a Discord server, you can create a new server using the link below.
Link: **https://www.howtogeek.com/318890/how-to-set-up-your-own-discord-chat-server/**

Inside Discord, right click on your server.
Goto "Server Settings", then "Webhooks".
Select "Create Webhook".
Give your bot a name, and choose which channel it will reside in.
Copy the provided Webhook Url (the Url can be accessed at anytime by clicking edit on your Webhook).

This is the Url you will need to put in the config.json file under webhookUrl