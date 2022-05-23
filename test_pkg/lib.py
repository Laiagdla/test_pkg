import urllib.request
from PIL import Image

def try_me():
    urllib.request.urlretrieve(
        'https://assets.sbnation.com/assets/3006205/office-space-printer-beat-down-gif.gif',
        "office-space-printer-beat-down-gif.gif")

    img = Image.open("office-space-printer-beat-down-gif.gif")
    img.show()
