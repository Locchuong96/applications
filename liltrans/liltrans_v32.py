from google_trans_new import google_translator  
import tkinter as tk
import pandas as pd
import pyttsx3

#print(googletrans.LANGUAGES)

head_text = """
English=en,Jap=ja,Chin=zh-cn,Viet=vi
[content]_[lang]
"""

translator = google_translator()
engine = pyttsx3.init()
engine.setProperty("rate", 110)


#Global var
new_word = []
speech_word = "" 


root= tk.Tk()
root.title("lil_trans v3.2 TECHAM_AI © ")
root.iconbitmap("./techam_ai.ico")

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

	engine.say(speech_word)
	engine.runAndWait()


button1 = tk.Button(text='Translate', command = Translate)
canvas1.create_window(50, 115, window=button1)

button2 = tk.Button(text='Speech_E', command = Speech)
canvas1.create_window(150, 115, window=button2)

button3 = tk.Button(text='Export', command = Export_new)
canvas1.create_window(250, 115, window=button3)


root.mainloop()