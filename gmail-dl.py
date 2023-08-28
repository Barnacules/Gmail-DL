import os
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import time
import datetime
import re

# Set up the OAuth 2.0 flow
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
creds = None

if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

if not creds or not creds.valid:
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
        token.write(creds.to_json())

# Connect to Gmail API
service = build("gmail", "v1", credentials=creds)

# Calculate the date 1 years ago from today
from_date = (datetime.datetime.now() - datetime.timedelta(days=365 * 20)).strftime(
    "%Y-%m-%d"
)

print(f"Looking for all emails since {from_date}")

# Search for emails with attachments from the last 10 years
query = f"has:attachment after:{from_date}"
page_token = None
all_messages = []
count = 0

while True:
    results = (
        service.users()
        .messages()
        .list(userId="me", q=query, pageToken=page_token)
        .execute()
    )
    messages = results.get("messages", [])

    if not messages:
        break

    count = count + len(messages)
    print(f"Emails Found: {count}", end="\r")
    all_messages.extend(messages)

    # Check if nextPageToken is missing or empty
    if "nextPageToken" not in results:
        print()
        break

    page_token = results.get("nextPageToken")

total_attachments = len(all_messages)
attachments_downloaded = 0

# Download attachments
start_time = time.time()

for idx, message in enumerate(all_messages, start=1):
    msg_data = service.users().messages().get(userId="me", id=message["id"]).execute()
    payload = msg_data["payload"]
    parts = ""

    # If parts is missing then just continue to the next time since something is messed up with this message
    if "parts" in payload:
        parts = payload["parts"]
    else:
        continue

    subject = None
    if "headers" in payload:
        for header in payload["headers"]:
            if header["name"] == "Subject":
                subject = header["value"]

    for part in parts:
        if part["filename"]:
            # Scrub filename so it doesn't screw with the local filesystem
            filename = re.sub(r'[\\/:*?"<>|]', "_", part["filename"])
            save_path = os.path.join("D:\\Temp\\email_attachments", filename)

            # Check if file is already downloaded and if so just skip it
            if os.path.exists(save_path):
                print(f"Skipping {filename} since it was already downloaded")
                continue

            # Make sure attachment ID is there before continuing since sometimes it's missing which is strange
            if part["body"].get("attachmentId") is None:
                print("Missing attachment ID, not sure why?!")
                continue

            attachment_id = part["body"]["attachmentId"]
            attachment = (
                service.users()
                .messages()
                .attachments()
                .get(userId="me", messageId=message["id"], id=attachment_id)
                .execute()
            )
            file_data = base64.urlsafe_b64decode(attachment["data"].encode("UTF-8"))

            print(
                f"Downloading attachment: {filename} from email with subject: {subject}"
            )

            with open(save_path, "wb") as f:
                f.write(file_data)

            attachments_downloaded += 1
            progress_percentage = (attachments_downloaded / total_attachments) * 100
            elapsed_time = time.time() - start_time
            avg_speed = attachments_downloaded / elapsed_time if elapsed_time > 0 else 0
            print(
                f"Progress: {progress_percentage:.2f}%, Elapsed Time: {elapsed_time:.2f} seconds, Avg Speed: {avg_speed:.2f} attachments/sec"
            )

print("Attachments downloaded successfully!")
