from moviepy.editor import *
import re


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

video_files = sorted_alphanumeric(os.listdir("final_videos"))

concatenate_videos = []
for i in video_files:
    video_file_clip = VideoFileClip("final_videos/" + i)
    concatenate_videos.append(video_file_clip)




final = concatenate_videoclips(concatenate_videos) # with gtts audio

audio = AudioFileClip("ADD YOUR OWN FILE CLIP!!!").fx(afx.volumex, 0.05) # !!!
loopedAudio = vfx.loop(audio,duration=final.duration)
final_audioclip = CompositeAudioClip([final.audio,loopedAudio])
final = final.set_audio(final_audioclip)
final.write_videofile("concatenated_video/concatenation.mp4") # added concatenated_video/ folder



print("final video CONCATENATION has been created.")