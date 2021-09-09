from datetime import datetime
import winsound
import docx
from gtts import gTTS

# replace it   

def read_doc(name):
	doc = docx.Document(name)
	content = []

	for paragraph in doc.paragraphs:
		content.append(paragraph.text)
	
	text = '\n'.join(content)
	text = text.replace(' ','')
	
	return text

if __name__ == "__main__":
	
	#print welcome
	print("Convert .docx file to .mp3! \n")

	# get file name
	doc_name = input("Enter your file's name: ")

	# starting counting time
	time_start = datetime.now()

	# get current time
	time= datetime.now()
	time = time.strftime("%Y%m%d_%H%M%S")

	try:
		#read text
		text = read_doc(doc_name)

		print("converting... \n")

		#create a speaker
		tts = gTTS(text = text, lang = 'vi')
		#sav
		tts.save(doc_name.replace('.docx','') + '.mp3')

	except Exception as e:
		print("Error: \n")
		print(e)
		for i in range(3):
			winsound.Beep(frequency = 600, duration = 300)

	# print out time execute
	time_done = datetime.now()
	print("I'm done, time for execution : {}".format(time_done - time_start))

	#beep sound
	winsound.Beep(frequency = 600, duration = 1000)