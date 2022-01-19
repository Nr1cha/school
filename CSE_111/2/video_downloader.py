import os 
import urllib.request
os.system("clear")
#https://www.youtube.com/watch?v=9H0Iopjrt1Y&ab_channel=SeanW
url = input("Enter the youtube-url\n")
name = input("Enter the name for the video\n")
name = name+".mp4"
try:
    print("downloading starting...\n")
    urllib.request.urlretrieve(url,name)
    print("Download completed! ")
except Exception as e:
    print(e)

