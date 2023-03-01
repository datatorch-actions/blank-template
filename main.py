import sys
import datatorch

from pytube import YouTube

if __name__ == "__main__":
    inputs = datatorch.get_inputs()
    url = inputs.get('url')

    youtubeObject = YouTube(url)
    youtubeObject  = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.download()
    except:
        print("Error with downloading YouTube video.")
        datatorch.set_output('completed', False)
        
    print("YouTube download successful.")
    datatorch.set_output('completed', True)
