### Description
This python script (./openRegistrations.py) will check the website defined in the config file (./config.json) and see if the search result (also in the config file) is on this website. If it is, then that means the registrations for that site are closed. If it is not, then the registration on that site are open. A discord message will be sent describing wether the registrations are open or closed. For best results, use cron to automate execution of this script.

The config file has the option to set quit times. This means that during these times the Discord message *will not be sent* for closed registrations only (open registrations supercede this setting and send Discord messages for open registrations regardless of the time of day). This is useful in the case that you want to set cron to run on the hour to continually check for open registrations, but only want to receive notifications about closed registrations during parts of the day. Say you want to run it on the hour, but only receive one notification per day about closed registrations, then you set your quite time for all hours of the day except one. If the start and end times for quite time are the same, quite time is disabled. 
Please note: quit times are in PST

To ensure best results, visit a site that does not have open registrations and copy part of that site which gives specification to their registrations being closed (examples can be found in ./config.json). If you copy the text from the site and receive incorrect results, be sure that the site doesn't have HTML encoding in the text. If it does, you will need to copy the HTML code for accurate results (example can be found in ./config.json).

### Settings
##### The only settings that will need changed are in config.json
webhookUrl: This is the webhook url for your discord bot. You can obtain a webhook url by going to your Discord, right clicking on your server, server settings > webhooks. Click "Create Webhook" and copy the provided url into the config file

quietTimeHours: Quit time disables Discord messages for closed registrations. Open registrations ignore quitTimeHours and send a message anyway.
    start: this is the time when quitTime will start (in PST)
    end: this is the time that quitTime will end (in PST)

checkMaintenance: Sometimes websites are down for maintenance meaning that the "search" query will not be found on the sight which provides a false positive that the registrations are open. To avoid this false positive, you can set checkMaintenance to 1. Otherwise, leave it as 0. Setting this to 1 could potentially (although unlikely) prevent from getting a tru positive result, so use at your own risk.

sendClosedNotifications: Options for this are 1 and 0. If 1, whenever the script is run, it is not quiet time and the registration is closed, a Discord message will be sent stating the site is closed. If set to 0, then there will never be Discord messages sent informing of a closed registration.

sites:
    name: The name of the site you want to search, only necessary for naming (can be left as a blank string)
    url: The url of the site you want to check (be sure that it is the registration part of the site. i.e. https://drunkenslug.com/***register***)
        search: This is the search string which will tell if the registrations are open or closed. Make sure it is a specific string from the site that says it is closed. It can be as simple as going to the registration part of the site and copyng their message which states the site is closed. If HTML is used in the site's description, you must use HTML in your search field. Example can be found in the config file for nzbplanet. 
    open: This field can be a 1 or a 0. If it is a 1, then the script will check if the site it open. If it is a 0, the script will ignore it altogether. This is handy if you get registered but want to keep  the config for the site in case a friend needs to get in later on but no longer want to receive messages about it.