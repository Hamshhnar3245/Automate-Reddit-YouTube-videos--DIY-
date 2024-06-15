# Automate Reddit YouTube videos (DIY)

## Introduction

Welcome to a stable public release of my RYTauto work. This repository will show you how to automate videos with your system yourself with minimal investment.

This is running in a medium-end pc so results could be different (16gb RAM | Intel® Core™ 17-13700H 3.7-5.0GHz | NVIDIA® RTX 4000 series) and the project will run in all systems with Windows OS 

I left some tips on how to do it with MacOS, but I haven't fully completed the project in this OS, so i'll say those are clues instead of tips.

## Getting Started

If running code in MacOS, don't forget to install HomeBrew.
- And remember: instead of ```pip install```, we ```brew install```  

You wont have any problems with following all these steps on Windows.

Virtual environments are not portable: you can install localy but it's not recomended. So if you us a venv, they will work for the operating system where you will run the project.

If you want to increase the comments, posts, etc. per video, you need to have in mind that Reddit offers free 60 API calls per minute.
- to enable API call terminal output: https://stackoverflow.com/questions/76529477/is-there-a-way-to-track-api-calls-through-praw

Automation in Windows OS is done using the task scheduler. I will leave some notes in the code on what code runs in the terminal so automation works properly.

ImageMagick (for the MoviePy part) is not strictly required, only if you want to write texts. It can also be used as a backend for GIFs but you can do GIFs with MoviePy without ImageMagick.
- Once you have installed it, ImageMagick will be automatically detected by MoviePy, except on Windows. 
- Windows user, before installing MoviePy by hand, go into the moviepy/config_defaults.py file and provide the path to the ImageMagick binary called magick. It should look like this: ```IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick_VERSION\\magick.exe"```

Check PRAW, Google Cloud documentation for more features of the APIs.

## How to run the script
0. Install all packages: check all py files for packages needed. 
1. Setup Google Cloud from Drive API
    1. Create Google Cloud project and set default variables.
    2. Install GCloud CLI: https://cloud.google.com/sdk/docs/install
    3. Setup Application Default Credentials: this video helped a lot in the Google Drive Setup: https://www.youtube.com/watch?v=cCKPjW5JwKo
2. Run in virtual environment (optional)
    1. Set execution momentary execution policy (if task is scheduled in WINDOWS: ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process```)
    2. in windows, type ```venv/Scripts/activate``` or in macOS: ```source venv/bin/activate```
    3. Stay on main directory
3. Start with ```Python_to_CSV.py``` file
    1. You can modifiy the code as you want, but for now it will ask for PRAW API credentials (user_agent, clinet_id, client_secret, username, password)
    2. Then the rest of the files will run after this python file.

## Thank you

Send me a message if assistance is needed. Thanks for checking my project out!

Aaron Arauco C.