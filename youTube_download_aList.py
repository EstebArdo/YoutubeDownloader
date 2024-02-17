import pytube
from pytube import YouTube
 
url_file = open(r"url_list.txt", "r")


print("################### Loop through the input ########### ")
with  url_file:
    n = 1
    for line in url_file:
        print(n, line.rstrip("\n"))
        n += 1
        # Add error handling for a blank line before download.
        YouTube(line).streams.first().download()




url_file.close()



#u="https://www.youtube.com/watch?v=C9vZL-xE4CQ"
#YouTube(u).streams.first().download()

"""
The following URL causes an error.
https://www.youtube.com/watch?v=kELhHQ4sC_Y

Add Error handling for it.

When I try to manually go to that page I get the message,
"Video unavailable"
"This video is not available"




"""
