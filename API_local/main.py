import tkinter as tk 
import json 
import datetime
import base64
import requests
import time


url_api   =  ""
userId    =  ""
timestamp =  ""
imageBlob =  ""

root = tk.Tk()
root.title("local_api VVSOLUTION © ")

canvas1 = tk.Canvas(root, width = 350, height = 250)
canvas1.pack()

entry_url = tk.Entry(root,width = 40)
entry_userId = tk.Entry(root,width = 40)
#entry_timestamp = tk.Entry(root,width = 40)
entry_imageBlob = tk.Entry(root,width = 40)

label_url = tk.Label(root)
label_url.config(text = "Url:")
label_userId = tk.Label(root)
label_userId.config(text = "UserId:")
label_timestamp = tk.Label(root)
label_timestamp.config(text = "TimeStamp:")
label_timenow = tk.Label(root)
label_imageBlob = tk.Label(root)
label_imageBlob.config(text = "ImageBlob:")
label_info = tk.Label(root)
label_info.config(text = "(^ - ^)")

canvas1.create_window(40,40,   window = label_url)
canvas1.create_window(200,40,  window = entry_url)
canvas1.create_window(40,70,   window = label_userId)
canvas1.create_window(200,70,  window = entry_userId)
canvas1.create_window(40,100,  window = label_timestamp)
canvas1.create_window(40,130,  window = label_imageBlob)
canvas1.create_window(200,130, window = entry_imageBlob)
canvas1.create_window(170, 200, window=label_info)

def send_api():

    global url_api 
    global userId   
    global timestamp 
    global imageBlob 

    url_api   = entry_url.get()
    userId    = entry_userId.get()
    timestamp = datetime.datetime.now().isoformat()
    imageBlob = entry_imageBlob.get()

    data = {
        "userId"   : userId,
        "timestamp": timestamp,
        "imageBlob": imageBlob
    }

    rep = requests.post(url_api, json = data)

    label_timenow.config(text = timestamp)
    canvas1.create_window(200,100,  window = label_timenow)

    label_info.config(text = rep)
    canvas1.create_window(170, 200, window=label_info)


button_send_api = tk.Button(text = "Send api",command = send_api)
canvas1.create_window(180,170, window = button_send_api)

root.mainloop()
