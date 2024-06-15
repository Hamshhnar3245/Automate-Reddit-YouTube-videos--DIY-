import os
from moviepy.editor import *
import re

print("Starting Audio files to singles mp4")

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

audio_files = sorted_alphanumeric(os.listdir("audio_samples"))
i = 1
for file in audio_files:
    os.rename("audio_samples/" + file, f'audio_samples/audio{i}.mp3')
    i+= 1

with open('data1.txt' , 'r') as data:
    lines = data.readlines()
    i = 1
for line in lines:
    if line != ', , , \n':
        try:
            duration = "audio_samples/audio%s.mp3" % i
            duration = AudioFileClip("audio_samples/audio%s.mp3" % i).duration
            center = TextClip(line, fontsize=50, color='white', font='Arial-Bold', size = (image_width*0.8,None),method='caption') 
            center_width , center_height = center.size
            center = center.set_position((image_width/2-center_width/2,image_height/2-center_height/2))
            final_video = CompositeVideoClip([bg_image, center] , size=bg_image.size)
            audio = AudioFileClip("audio_samples/audio%s.mp3" % i) 
            final_video = final_video.set_audio(audio)
            final_video = final_video.set_duration(audio.duration)
            final_video.write_videofile("final_videos/final_video%s.mp4" % i , fps = 2,) # feel free to increase fps, but performance of cpu will take a hit!
            i = i + 1
        except OSError as error:
            print(error)
            i = i + 1
            pass
data.close()

print("Audio files converted to final_videos DONE.")


# Next .py file:
import singles_mp4_to_video_concatenator