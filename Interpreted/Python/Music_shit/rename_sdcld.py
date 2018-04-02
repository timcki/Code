import os
import sys

def rename():
	if len(sys.argv) < 2:
		usage()

	path: str = sys.argv[1]

	filenames = next(os.walk(path))[2]

	for i in filenames:
		os.rename(i, "{}.{}".format(i.split('-')[0], "mp3"))
rename()
