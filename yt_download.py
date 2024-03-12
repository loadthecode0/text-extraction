from pytube import YouTube

def Download():
    youtubeObject = YouTube("https://www.youtube.com/watch?v=GCdwKhTtNNw")
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
Download()