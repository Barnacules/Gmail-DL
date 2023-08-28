# Google Gmail Attachment Downloader

## Description
This is prototype code to download all the attachments from a target gmail account for a given start date to present date outline in the actual source code that needs to be changed prior to execution until I have to time to polish this program with all the command line variables that everyone deserves. I created this on a whim in a few minutes from an idea given to me on Twitter from one of my followers named @DukeRamze on Twitter so be sure and thank him for the idea

## Requirements
I included a requirements.txt file so just run (*pip install -r requirements.txt*)

## How to use program
1. Clone respository or download **requirements.txt** & **gmail-dl.py** locally
2. Install Requirements (pip install -r requirements.txt)
3. Go to Google Cloud -> APIs & Services > OAuth Consent Screen
   - https://console.cloud.google.com/apis/credentials/consent
4. Create a Consent Screen for your new app
5. Add the account you want to download the emails from under "test users" for your app you just created
6. Download the credentials.json from the app and put it in the same folder as Gmail-DP.py
7. ***TEMPORARY***: Modify the date around line 30 with the number of days or date you want to start downloading attachments
8. ***TEMPORARY***: Modify the destination folder around line 77 to change the folder where the attachments will be stored
9. Run Gmail-dl.py (**python3 gmail-dl.py**)

## State of project
I have about 30 minutes tied up into this source code thanks to ChatGPT 🙏 The code does work but it requires you to create your own Google API endpoint and use Google Authentication since I needed this code to work with 2FA for my purposes otherwise it could be greatly simplified down to email/password if you enable the "allow older apps" security option in your Google Dashboard for the account you want to download the attachments from. Feel free to fork the code and modify it as you see fit. I just wrote this because a fan asked if I had a program that could do this and I decided to take a wack at it.

## Contact me
If you enjoy this or have questions hit me up over on Twitter @barnacules since I probably won't get around to polishing this program for some time. Who knows, maybe I'll do it during my Twitch live stream 😉

