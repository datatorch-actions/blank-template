import sys
import datatorch

from pytube import YouTube

if __name__ == "__main__":
    inputs = datatorch.get_inputs()
    url = inputs.get('url')
    path = inputs.get('path')

    youtubeObject = YouTube(url)
    youtubeObject  = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.download(path)
    except:
        datatorch.set_output('completed', False)
        raise Exception("Error with downloading YouTube video.")

    print("YouTube download successful.")
    datatorch.set_output('completed', True)
