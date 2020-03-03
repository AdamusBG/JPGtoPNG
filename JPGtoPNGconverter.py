import sys     #will need sys to get file paths from the command line
import os      #os needed to manipulate files
from PIL import Image      #needed for the final stage to manipulate the images


filepath1 = sys.argv [1]
filepath2 = sys.argv[2]

if not os.path.isdir(filepath2):
	try:
		os.mkdir(filepath2)
	except FileNotFoundError:
		print("FileNotFoundError - Please carefully check the file path entered and verify that it is valid.")

for filename in os.listdir(filepath1):
	try:
		img = Image.open(f'{filepath1}{filename}')
		trimname = os.path.splitext(filename)[0]
		img.save(f'{filepath2}{trimname}.png', 'png')
	except FileNotFoundError:
		print("FileNotFoundError - make sure both file paths end with \'/\'")
		break