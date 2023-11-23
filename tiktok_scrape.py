from tiktokapipy.api import TikTokAPI

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

# Create a DataFrame
data = {
    'Challenge_ID': challenge_ids,
    'Challenge_Title': challenge_titles,
    'Video_ID': video_ids,
    'Video_Description': video_descriptions,
    'Comment_Text': comment_texts
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)