**Gmail-DL.py is a program that will download all the attachments from an authenticated gmail account for a given time period**

1. Install Requirements (pip install -r requirements.txt)
2. Go to Google Cloud -> APIs & Services > OAuth Consent Screen
   - https://console.cloud.google.com/apis/credentials/consent
3. Create a Consent Screen for your new app
4. Add the account you want to download the emails from under "test users" for your app you just created
5. Download the credentials.json from the app and put it in the same folder as Gmail-DP.py
6. TEMPORARY: Modify the date on line 30 with the start date you want to download attachments from
7. TEMPORARY: Modify line 77 to change the folder where the attachments will be stored
8. Run Gmail-dl.py (python3 gmail-dl.py)

If you did everything correctly it should start downloading emails but wait until it's fully donw downloading before looking for the attachments since it won't create the attachments themselves until it's finished querying all the emails because this is some very quickly thrown together code that when I have more time I will optimize the hell out of and put a bunch of command line options on so everyone can use it much easier. I'll also see if I can publish the Google App so people can authenticate with it without having to create their own google app and credentials.json file and will only have to request access to get the token.json file. The program will also prompt you when you first run it to pick the gmail account you want to download the emails from on the authentication screen you created earlier with your app. If you select an accout that you didn't add as a test user it will error out and give you problems. This code is very fragile so use at your own risk and also realize it will download attachments with viruses so make sure you have a good antivirus or download in a vaccuum just to be safe.

Enjoy, this idea was given to me by @DukeRamze on Twitter about an hour ago and figured I would throw something together for him and others that at least some kind of basic code that works to download attachments. 

**TROUBLE SHOOTING**
If you get an error saying it doesn't have access to something after it authenticates successfully you might have to go into API's for your app and search for "Gmail API" and Enable it because for some reason it's not added by default sometimes. Once you add this it should start working and count up when you run it. Start with a lesser date then 1 year which is the default setting I have right now until you have it tuned and working right so you don't waste so much time on each run.

Oh, and feel free to add to the code as you see fit, this is just a quick project I created in a few minutes to get something working as a baseline to help others. This is about as unpolished of a prototype as you can get!

Hit me up on gmail if you do something cool with this http://twitter.com/barnacules
