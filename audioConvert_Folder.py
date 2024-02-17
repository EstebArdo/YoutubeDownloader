#####################################################################
import os
import shutil
from moviepy.editor import *

###################################################################
def MakeMp3(): 
  videoClip = VideoFileClip(file_name)
  AudioClip = videoClip.audio  
  file_name_base, file_ext = os.path.splitext(file_name)
  print(file_name_base)
  mp3_file = file_name_base + ".mp3" 
  AudioClip.write_audiofile(mp3_file)
  AudioClip.close()
  videoClip.close()        

###################################################################

###################################################################
def delete_destination_mp4_files():
  for dest_file in os.listdir(destination_path):
      if '.mp4' in dest_file[-4:]:
         print (dest_file + " HAS MP4")
         if os.path.exists(destination_path + dest_file):
            os.remove(destination_path + dest_file) 
         else:
             print("File not found" + dest_file)
             print(destination_path + dest_file)
      else:
         print (" NOT mp4 NNNNNNNNNNNNNNNNNNNN   " + dest_file  )
###################################################################  


dir_list = os.listdir() 
print("############### Files and directories in current folder:")


for file_name in os.listdir():
    if file_name.endswith(".mp4"):
        print(file_name)
        MakeMp3()

current_directory = os.getcwd()
destination_path = "C:/Users/Steve/Music/pytubeOut/"
dir_list = os.listdir()

###################################################################
print("#################### Move mp3 and mp4 files only. ####################")
for file_name in dir_list:
    if '.mp4' in file_name or '.mp3' in file_name :      
      shutil.move(file_name,destination_path + file_name)
    else:
      print("not media - " + file_name)


###################################################################
# delete the file
# os.remove(file_path)      

# Right 2 characters
# string[-2:]
print("#################### Optionally Delete mp4 files only. ####################")  
delete_destination_mp4_files()  
