from tiktokapipy.api import TikTokAPI
import pandas as pd
from playwright.sync_api import playwright

import time

# Initialize empty lists to store data
challenge_ids = []
challenge_titles = []
video_ids = []
video_descriptions = []
comment_texts = []

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

                    # Append data to lists
                    challenge_ids.append(challenge_name)
                    challenge_titles.append(challenge.title)
                    video_ids.append(video.id)
                    video_descriptions.append(video.desc)
                    comment_texts.append(comment.text)

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
    'Challenge_ID': challenge_ids,
    'Challenge_Title': challenge_titles,
    'Video_ID': video_ids,
    'Video_Description': video_descriptions,
    'Comment_Text': comment_texts
}

df = pd.DataFrame(data)

# Print lengths
print(f"Number of Challenges: {len(challenge_ids)}")
print(f"Number of Videos: {len(video_ids)}")
print(f"Number of Comments: {len(comment_texts)}")

# Print the DataFrame
print(df.to_string())

