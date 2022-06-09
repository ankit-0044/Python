# Instagram profile downloder

import instaloader  

bot = instaloader.Instaloader()             # Get Instance

username = input("Enter username: ")        # Ask for user name

download = bot.download_profile(username, profile_pic_only=True)            # Download the picture

print("Download Successful")