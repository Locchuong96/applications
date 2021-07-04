import webbrowser
import time
import os 

print("----------[[ WELLCOME TO MIMI VIEW ver1.0 ]]----------")
print("-------[[ DEVELOPED BY TECHAM_AI copyright © ]]-------")
print("\n")

url = input("Enter link of video: ")
time_sleep = int(input("Enter time of video: "))
no = int(input("Enter views of video: "))

print("EXCUTE...")

for i in range(no):

	print("Time {}: RUNING...".format(i))

	webbrowser.open(url)

	time.sleep(time_sleep)

	os.system("taskkill /im chrome.exe /f")

print("DONE...")

