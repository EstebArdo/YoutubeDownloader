from pytube import Playlist
url="https://www.youtube.com/playlist?list=PLEUbaQHXBFXpmx5GbskGlOCneQcIqNhuI"
pl=Playlist(url)
#print(type(pl))

print("\n\n +++++++++++++++++++++++++++++++++++++++++")
print(pl)
print("\n\n +++++++++++++++++++++++++++++++++++++++++")
# pl.description
# pl.views
# pl.title
#'Country 2024'
# pl.owner
#'by ChocoLovesMusic'
# pl.owner_id
#'UC-c9iHM6rD0LPAHHDx1RLvA'
# pl.owner_url
#'https://www.youtube.com/channel/UC-c9iHM6rD0LPAHHDx1RLvA'
#  pl or pl.video_urls  >>gives a list of the video urls from the playlist.
#  len(pl) is number of videos in playlist.
print("\n Playlist Title : " + pl.title)
#################################################################
## Videos can be used to access each video in playlist
# video=pl.videos[0]
# video.title
#'Thank God'
#video=pl.videos[1]
#video.title
#'Thought You Should Know'
# video.views
#################################
# for v in pl.videos # to loop through the videos
# v.watch_url is the url to the video to watch it or download it.
############
for v in pl.videos:
   print(v.author)
   print(v.watch_url)

