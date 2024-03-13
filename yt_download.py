from pytube import YouTube

def Download():
    youtubeObject = YouTube("https://www.youtube.com/watch?v=4boWV-Ba4Vw")
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


Download()