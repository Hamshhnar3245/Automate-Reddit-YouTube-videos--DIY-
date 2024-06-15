import csv
from gtts import gTTS
import shutil

print("Starting CSV to Audio files")

with open('data1.csv', 'r') as read_obj: # read csv file as a list of lists
  dict = {}
  csv_reader = csv.reader(read_obj) # pass the file object to reader() to get the reader object
  for rows in csv_reader:
     print(rows)
     if len(rows) == 0: # when rows is an empty list
       pass
     else:
       dict[csv_reader.line_num] = str(rows) 


with open("data1.txt" , "w") as txt_file:
    for element in dict:
      txt_file.write(str(dict[element])+ "\n")


for element in dict:
  clear_element = dict[element].strip('[]').replace("'","")
  if clear_element == ', , , ':
     pass
  else:
    tts = gTTS(str(dict[element].strip('[]').replace("'","")))
    try:
        tts.save('audio_samples/' + 'sample%s.mp3' % element)
    except AssertionError:
      pass


print("Audio files have been created")


# Next .py file:
import Audio_files_to_singles_mp4

