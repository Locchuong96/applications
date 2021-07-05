from   googletrans import Translator 
import tkinter as tk
import pandas as pd
from   gtts import gTTS
import os
from   bs4 import BeautifulSoup 
import requests
import urllib.request
import PIL.Image
import wikipedia


head_text = """
Eng=en,Jap=ja,Chin=zh-cn,Viet=vi
[content]_[lang]
"""

translator = Translator()

#Global var
new_word = []
# speech_word = ""
content     = "" 


root= tk.Tk()
root.title("liltrans.v3.4 TECHAM_AI©")
root.attributes('-alpha',0.7)
#root.iconbitmap("./techam_ai.ico")

canvas1 = tk.Canvas(root, width = 260, height = 200)
canvas1.pack()

entry1 = tk.Entry(root,width = 40) 
canvas1.create_window(130, 75, window=entry1)

label1 = tk.Label(root, text= head_text)
canvas1.create_window(130, 30, window = label1)

label2 = tk.Label(root)
label2.config(text= "")

def Translate():
	global new_word
	global content
	text_in  = entry1.get()
	content  = text_in.split("_")[0]
	lang     = text_in.split("_")[-1]
	#text_out = translator.translate(content,lang_tgt=lang)	
	text_out = translator.translate(content,dest = lang).text
	new_word.append([content,text_out])
	label2.config(text= text_out)
	canvas1.create_window(150, 170, window=label2)
    
def Export_new():
	global new_word
	df = pd.DataFrame(new_word)
	df.to_excel("./New_word.xlsx")
	label2.config(text= "Exported!")
	canvas1.create_window(200, 170, window=label2)

def Speech():
	"""
	Get the content at input field
	"""
	text_in  = entry1.get()
	content  = text_in.split("_")[0]
	tts      = gTTS(content)
	tts.save('audio.mp3')
	os.system('audio.mp3')

def Image():
	"""
	Get the content at input field
	"""
	text_in   = entry1.get()
	content   = text_in.split("_")[0]
	link      = 'https://www.google.com/search?q=' + content + '&' + 'tbm=isch'
	page      = requests.get(link)
	soup      = BeautifulSoup(page.text,'lxml')
	imgs      = soup.find_all('img')
	img_first = imgs[1].get('src')
	urllib.request.urlretrieve(img_first,'image.png')
	img       = PIL.Image.open('image.png')
	img.show()

def Wikipedia():
	"""
	Get the content at input field
	"""
	text_in = entry1.get()
	content = text_in.split("_")[0]

	wikipedia.set_lang("en")
	summary = wikipedia.summary(content,sentences = 2)
	# Read it
	tts     = gTTS(summary)
	tts.save('summary.mp3')
	os.system('summary.mp3')



button1 = tk.Button(text='Trans', command = Translate)
canvas1.create_window(30, 115, window=button1)

button2 = tk.Button(text='Talk', command = Speech)
canvas1.create_window(175, 115, window=button2)

button3 = tk.Button(text='Export', command = Export_new)
canvas1.create_window(230, 115, window=button3)

button4 = tk.Button(text='See', command = Image)
canvas1.create_window(80, 115, window=button4)

button5 = tk.Button(text='Sum', command = Wikipedia)
canvas1.create_window(126, 115, window=button5)

root.mainloop()