import os
os.system("call venv_win/Scripts/activate") # delete if not automating it. helps Window's task scheduler start the virtual environment.

import re
import praw
import csv
import time
import emoji

import Audio_files_to_singles_mp4
import CSV_to_Audio_files
import googledrive_to_deleteCurrentMedia
import Scheduled_gmail_alert
import singles_mp4_to_video_concatenator
import videoConcatenator_to_googledrive

print("WELCOME TO Automate Reddit YouTube videos (DIY)!")


def RedditVideoScript(wwww, password2 = "qqqqqqqqqqq"): # qqqqqqq is no flag at start of post hehe

    praw_user_agent = input("praw user_agent: ")
    praw_client_id = input("praw client_id: ")
    praw_client_secret = input("praw client_secret: ")
    praw_username = input("rReddit username: ")
    praw_password = input("password of account: ")

    reddit = praw.Reddit(user_agent=praw_user_agent,   # 'Aaron' for example
                         client_id=praw_client_id, 
                         client_secret=praw_client_secret, 
                         username=praw_username, password = praw_password)

    subreddits_count = int(input("How many subreddits do you want to compile (recommended range: [1-5]. recommended output: 2)? "))

    def char_is_emoji(character):
        return emoji.is_emoji(character)


    with open("data1.csv" , mode = "w") as data_file:
        header = ["a","b","c","d"]
        writer = csv.DictWriter(data_file , fieldnames=header)

        for subreddit_count in range(subreddits_count):
            subreddit_name = input("What is the name of the subreddit you want to scrape (on the url)? ") # for now, AmItheAsshole
            # subreddit_name = wwww
            subreddit = reddit.subreddit(subreddit_name)
            posts_count = int(input("How many post do you want to scrape from this subreddit (recommended range: [1-5]. Recommended output: 2)? "))
            print("We will output" , posts_count , "posts out of the hottest ones of the last 24 hours.")
            comments_count = int(input("How many comments per post would you like to scrape? "))
            # comments_count = 8     this is the amount of comments i requested from AmItheAsshole
            print("Scraping...")

            for submission in subreddit.search(subreddit,limit=posts_count,time_filter="day",sort="top"): # submissions are posts.
                submission_title = reddit.submission(submission).title
                for i in submission_title:
                    if char_is_emoji(i):
                        submission_title = submission_title.replace(i,"")
                submission_author = reddit.submission(submission).author

                writer.writerow({"a":submission_title , "b": subreddit , "c":submission_author})
                print("Subreddit, Subredit title, Subreddit author READY.")
            
                for comment in range(0,comments_count):
                    try:
                        # submission.comments[comment].body
                        comment_body = submission.comments[comment].body
                        comment_body = comment_body.replace("\n","") # to avoid newline's when writing into csv.
                        for i in comment_body:
                            if char_is_emoji(i):
                                comment_body = comment_body.replace(i,"")
                        comment_author = submission.comments[comment].author

                        if comment_body.startswith(password2):
                            continue
                        else:
                            writer.writerow({"a":"""""""" + comment_body + """""""" , "b":comment_author , "c":submission.comments[comment].score})
                            print("Comment, Comment author, Comment score READY.")
                    except:
                        continue
                    
                writer.writerow({"a":""})

    data_file.close()

os.system("python googledrive_to_deleteCurrentMedia.py")

#AmItheAsshole
RedditVideoScript("AmItheAsshole" , password2 = "Welcome to") # flag for password2 is "Welcome to" because subreddit has always starting index comment THAT NEEDS TO BE AVOIDED.
print("Running script for r/AmItheAsshole")
# Next .py file(s):
os.system("python Scheduled_gmail_alert.py")
os.system("python CSV_to_Audio_files.py")
time.sleep(20)


