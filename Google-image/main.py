import google_image
import PIL.Image

# create your finder
finder = google_image.google_image1()

# enter your keyword
keyword = input('What do you want to find: ')

# get the image
img = finder.find(keyword)

# Show your keyword
img.show()
