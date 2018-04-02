#! /usr/bin/python3

#
# Utility to rename files downloaded from youtube by yt-dl. Broken for now
#

import os
import sys
from typing import List

def usage():
	print("USAGE: ./rename.py dir")
	print("Renames files for yt-dl, removing url artifacts")
	quit()

def split_name(filenames: List[str]):
	a = []
	for name in filenames:
		a.append(name.split('-'))
	return a

# leaves room for improvement. Maybe tag support natively
def get_extension(filename):
	if  "webm" in filename:
		return "webm"
	elif "mp3" in filename:
		return "mp3"
	elif "flac" in filename:
		return "flac"
	else:
		return Filetype.unknown

def set_tags(filename: str, run_with_rename: List[str]):
	import subprocess
	if run_with_rename:
		subprocess.run(["/usr/local/bin/tag", run_with_rename[0], name_after_change, run_with_rename[1], run_with_rename[2]])
	else:
		subprocess.run(["/usr/local/bin/tag", 


def main():
	if len(sys.argv) < 2:
		usage()

	path: str = sys.argv[1]

	# get filenames (non-recursive)
	# TODO implement recursion
	# third value only -> [2]
	filenames = next(os.walk(path))[2]

	names = split_name(filenames)

	# Test if the output is not broken (egde cases)
	choice = input("Rename or dry run? (D|R): ")

	if choice == 'R':
		choice = input("Set tags based on filename? (Y|N): ")
		for a, name in zip(names, filenames):
			ext = get_extension(a[-1])
			name_after_change = "{}/{} - {}.{}".format(path, a[0].strip(), a[1].strip(), ext)
			os.rename("{}/{}".format(path, name), name_after_change)
			if choice == 'Y' or choice == 'y':
				import subprocess
				subprocess.run(["/usr/local/bin/tag", ext, name_after_change, a[0].strip(), a[1].strip()])

	elif choice == 'D' or choice == 'd':
		for a,name in zip(names, filenames):
			ext = get_extension(a[-1])
			print("{} -> {} - {}.{}".format(name, a[0].strip(), a[1].strip(), ext))


	else:
		print("Done!")
		quit()

main()
# Broken for now 


