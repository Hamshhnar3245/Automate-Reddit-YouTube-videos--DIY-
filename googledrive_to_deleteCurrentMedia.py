import os

import time


audio_files = os.listdir("audio_samples")

for i in audio_files:
    os.remove("audio_samples/%s" % i)
    print("audio_samples/%s got deleted." % i)

video_files = os.listdir("final_videos")
for i in video_files:
    os.remove("final_videos/%s" % i)

conctenated_video = os.listdir("concatenated_video")
# time.sleep(120)
for i in conctenated_video:
    os.remove("concatenated_video/%s" % i)

print("audio files, video files, and concatenated video files have been deleted.")