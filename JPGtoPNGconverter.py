import sys     #will need sys to get file paths from the command line
import os      #os needed to manipulate files
from PIL import Image      #needed for the final stage to manipulate the images

filepath1 = sys.argv [1]
filepath2 = sys.argv[2]

if os.path.isdir(filepath2):
	pass
else:
	try:
		os.mkdir(filepath2)
	except FileNotFoundError:
		print("Please carefully check the file path entered and verify that it is valid.")