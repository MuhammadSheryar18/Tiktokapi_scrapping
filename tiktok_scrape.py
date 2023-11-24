from tiktokapipy.api import TikTokAPI
import pandas as pd
from playwright.sync_api import playwright  # Add this import

import time

retries = 3
for attempt in range(retries):
    try:
        # Initialize the TikTokAPI instance
        with TikTokAPI() as api:
            # Scrape data for the 'blasphemy' challenge
            challenge_name = 'blasphemy'
            challenge = api.challenge(challenge_name)

            # Accessing challenge information
            print(f"Challenge ID: {challenge_name}")
            print(f"Challenge Title: {challenge.title}")

            # Retrieve videos related to the challenge
            videos = challenge.videos

            # Loop through each video related to the challenge and fetch comments and descriptions
            for video in videos:
                print(f"Video ID: {video.id}")
                print(f"Video Description: {video.desc}")

                # Fetch comments for the video
                comments = video.comments
                print(f"Comments for Video {video.id}:")
                for comment in comments:
                    print(comment.text)
                break  # If successful, exit the loop
    except playwright._impl._errors.TimeoutError:
        if attempt < retries - 1:
            print(f"Attempt {attempt + 1} failed. Retrying...")
            time.sleep(2)  # Add a small delay before retrying
        else:
            print("All attempts failed. Exiting.")
            raise  # Re-raise the exception if all attempts fail

# Create a DataFrame
data = {
    'Challenge_ID': [challenge_name],
    'Challenge_Title': [challenge.title],
    'Video_ID': [video.id],
    'Video_Description': [video.desc],
    'Comment_Text': [comment.text]
}

df = pd.DataFrame(data)

print(df)



