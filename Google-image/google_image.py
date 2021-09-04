from bs4 import BeautifulSoup
import requests
import urllib.request
import PIL.Image

class google_image1:
    def __init__(self):
        pass
    
    def find(self,keyword):
        """
        find the image follow the keyword
        """
        link = 'https://www.google.com/search?q=' + keyword + '&' + 'tbm=isch'
        page = requests.get(link)
        soup = BeautifulSoup(page.text,'lxml')
        imgs = soup.find_all('img')
        img_first = imgs[1].get('src')
        #rint(img_first)
        urllib.request.urlretrieve(img_first,'google_image1.png')
        img = PIL.Image.open('google_image1.png')
        return img
