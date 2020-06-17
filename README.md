### Description
This Python script is designed to check private websites to see if they currently have open registrations and then send a Discord message via a bot informing users of the website's current state. There will be one Discord message for each site that is set to be checked in the config file.

To do so, the script looks at the website's registration page and checks if it has a specific string which defines that it is closed. For example, if the phrasing "Open registrations are currently closed. You will need an invite code to join" is found on the page, then the site is closed. However, if this phrase is not found on the website, the site is open. 

This method can return a false positive in two scenarios:
    1. The site owner has chosen to change the wording of their site
    2. The site is down for maintenance

The first false positive cannot be avoided, and users will have to update their settings in order to fix this false positive if it occurs.
The second false positive can be limited. To do so, the user can define a *check for maintenance* setting to be true or false. If set, the script will then check for the word "maintenance" in the site's HTML. If found, the false positive will not occur. This setting has not been thoroughly tested, so ***use at your own risk***

The user has the option to set a quiet time for the script. During this time, there will be no Discord messages sent for *closed* registrations. *Open* registrations will ignore this quiet time and a Discord message will always be sent if a website is found to have *open* registration. Quiet time is set only by hours (no minutes or seconds) and it is in a 24hr format.
***Note: quiet time is set in PST***
Quiet time can be used to fit the following scenario:
The user wants to only receive one notification per day if the site is closed. But, the user also wants to run the script once an hour to be immediately notified of open registrations. In this case, the user can set his quiet time from 01 until 24. When the script runs at 00 it will send a message stating the site is closed (granted that is the case). The 23 other times it runs that day, no notifications will be sent unless the site has open registrations.

The user has the option to configure alerts for closed registrations. If enabled, every time the script is ran a Discord message will be sent stating the current condition of registration for the website. If disabled, the script will only send a Discord message if the website's registration is *open*.

To ensure best results when setting up your config file, visit a site that currently has closed registrations. Find a defining piece of text on their site that says their registration is closed, and copy that into your config file. Some sites will inject HTML into these messages (an example of this is seen in the provided config file). In these cases, you will need to copy the HTML code for the message and not just the text. Using the link below, you can view the HTML code in Chrome and copy it from there (if you don't have Chrome, a quick search online will help you learn to do it in your browser of choice).
Link: **https://www.lifewire.com/view-html-source-in-chrome-3466725**

### Settings
##### The only settings that will need changed are in config.json
**webhookUrl**: This is the webhook url for your discord bot. You can obtain a webhook url by going to your Discord, right clicking on your server, server settings > webhooks. Click "Create Webhook" and copy the provided url into the config file

**quietTimeHours**: Quit time disables Discord messages for closed registrations. Open registrations ignore quitTimeHours and send a message anyway.
    start: this is the time when quitTime will start (in PST)
    end: this is the time that quitTime will end (in PST)

**checkMaintenance**: Sometimes websites are down for maintenance meaning that the "search" query will not be found on the sight which provides a false positive that the registrations are open. To avoid this false positive, you can set checkMaintenance to 1. Otherwise, leave it as 0. Setting this to 1 could potentially (although unlikely) prevent from getting a tru positive result, so use at your own risk.

**sendClosedNotifications**: Options for this are 1 and 0. If 1, whenever the script is run, it is not quiet time and the registration is closed, a Discord message will be sent stating the site is closed. If set to 0, then there will never be Discord messages sent informing of a closed registration.

**sites**:
    **name**: The name of the site you want to search, only necessary for naming (can be left as a blank string)
    **url**: The url of the site you want to check (be sure that it is the registration part of the site. i.e. https://drunkenslug.com/***register***)
        search: This is the search string which will tell if the registrations are open or closed. Make sure it is a specific string from the site that says it is closed. It can be as simple as going to the registration part of the site and copyng their message which states the site is closed. If HTML is used in the site's description, you must use HTML in your search field. Example can be found in the config file for nzbplanet. 
    **open**: This field can be a 1 or a 0. If it is a 1, then the script will check if the site it open. If it is a 0, the script will ignore it altogether. This is handy if you get registered but want to keep the config for the site in case a friend needs to get in later on but no longer want to receive messages about it.

### Obtaining a Discord Webhook Url
To get a Discord Webhook Url, you will need to be managing a Discord server. You can create your own if you don't already have access to one (**https://www.howtogeek.com/318890/how-to-set-up-your-own-discord-chat-server/**).

Inside Discord, right click on your server.
Goto "Server Settings", then "Webhooks".
Select "Create Webhook".
Give your bot a name, and choose which channel it will reside in.
Copy the provided Webhook Url (the Url can be accessed at anytime by clicking edit on your Webhook).

This is the Url you will need to put in the config.json file under webhookUrl