import pytube
from pytube import YouTube
from pytube import Playlist

playlist_url="https://www.youtube.com/playlist?list=PLEUbaQHXBFXpmx5GbskGlOCneQcIqNhuI"
pl=Playlist(playlist_url) 
url_file = open(r"url_list.txt", "w")

print("\n\n +++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("   Playlist to write to file: " + pl.title)
print("\n +++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

for v in pl.videos:
   print(v.title)  
   url_file.write(v.watch_url +"\n")

url_file.close()
print("\n ++++++++++++++ Finished creating URL file +++++++++++++++ \n ")
 

    

 
 
 