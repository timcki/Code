#! /usr/bin/mksh

for entry in "$1"/*
do
	without_webm=$( echo "$entry" | grep -oP ".+ - [^\.]*")
	ffmpeg -i "$entry" "${without_webm}.flac"
	echo "DONE: ${entry} -> ${without_webm}.flac"
done

