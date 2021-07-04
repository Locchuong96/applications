from google_trans_new import google_translator  
import tkinter as tk
import pandas as pd
from gtts import gTTS
import os
from bs4 import BeautifulSoup 
import requests
import urllib.request
import PIL.Image


head_text = """
Eng=en,Jap=ja,Chin=zh-cn,Viet=vi
[content]_[lang]
"""

translator = google_translator()

#Global var
new_word = []
speech_word = "" 


root= tk.Tk()
root.title("lil_trans v3.3 TECHAM_AI © ")
#root.iconbitmap("./techam_ai.ico")

canvas1 = tk.Canvas(root, width = 300, height = 200)
canvas1.pack()

entry1 = tk.Entry(root,width = 40) 
canvas1.create_window(150, 75, window=entry1)

label1 = tk.Label(root, text= head_text)
canvas1.create_window(150, 30, window = label1)

label2 = tk.Label(root)
label2.config(text= "")

def Translate():

	global new_word
	global speech_word

	text_in = entry1.get()
	content  = text_in.split("_")[0]
	lang     = text_in.split("_")[-1]
	 
	text_out = translator.translate(content,lang_tgt=lang)
	#translator = Translator(to_lang = lang)
	#text_out = translator.translate(content,dest = lang)	

	new_word.append([content,text_out])
	speech_word = content

	label2.config(text= text_out)
	canvas1.create_window(150, 170, window=label2)
    
def Export_new():

	global new_word
	
	df = pd.DataFrame(new_word)

	df.to_excel("./New_word.xlsx")

	label2.config(text= "Exported!")
	canvas1.create_window(200, 170, window=label2)

def Speech():
	global speech_word

	tts = gTTS(speech_word)
	tts.save('audio.mp3')
	os.system('audio.mp3')

def Image():
	global speech_word
	link = 'https://www.google.com/search?q=' + speech_word + '&' + 'tbm=isch'
	page = requests.get(link)
	soup = BeautifulSoup(page.text,'lxml')
	imgs = soup.find_all('img')
	img_first = imgs[1].get('src')
	urllib.request.urlretrieve(img_first,'image.png')
	img = PIL.Image.open('image.png')
	img.show()

button1 = tk.Button(text='Translate', command = Translate)
canvas1.create_window(50, 115, window=button1)

button2 = tk.Button(text='Speech_E', command = Speech)
canvas1.create_window(182, 115, window=button2)

button3 = tk.Button(text='Export', command = Export_new)
canvas1.create_window(250, 115, window=button3)

button4 = tk.Button(text='Image', command = Image)
canvas1.create_window(115, 115, window=button4)

root.mainloop()