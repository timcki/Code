#! /usr/bin/mksh

case $1 in

	mp3)
		file="tmp.mp3";;
	webm)
		file="tmp.webm";;
	flac)
		file="tmp.flac";;
esac

ffmpeg -i "$2" -c copy -metadata title="$4" -metadata artist="$3" "${file}" 2>/dev/null 1>/dev/null && (rm "$2" && mv "${file}" "$2" && echo "$2: Good") || (echo "$2: Failed")
