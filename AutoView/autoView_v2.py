import webbrowser
import time 
import datetime
import os
from tqdm import trange

print("-------[[ DEVELOPED BY TECHAM_AI copyright © ]]-------")
print("----------[[ WELLCOME TO MIMI VIEW ver2.0 ]]----------")
print("----------------[[ ************** ]]------------------")
print("\n")

time_start = str(datetime.datetime.now())

url = input("Enter link of video: ")
time_sleep = int(input("Enter time of video: "))
no = int(input("Enter views of video: "))
time_step = 1 # second

print("EXCUTE...")

for i in range(no):

	print("Time {}: RUNING...".format(i))

	webbrowser.open(url)

	#Delay for excuting the progress bar
	# pbar = tqdm(total  = time_sleep)
	# for j in range(time_sleep):
	# 	time.sleep(time_step)
	# 	pbar.update(time_sleep/(time_step * j + 1))

	for j in trange(time_sleep):
		time.sleep(time_step)

	os.system("taskkill /im chrome.exe /f")

	time_end = str(datetime.datetime.now())

print("DONE from {0} to {1}".format(time_start[0:19],time_end[0:19]))
print("THANK YOU FOR USING!!!")