#! /usr/bin/mksh

# a bit of a code refactor. Now display value as string passed to notification so they stack on top of each other

case $1 in
	up)
		amixer -q set Master 2+
		value=$(amixer get Master | grep -oP '[0-9]+\%')
		notify-send -a "Volume" -u low "Volume" -h int:value:$value
		;;
	down)
		amixer -q set Master 2-
		value=$(amixer get Master | grep -oP '[0-9]+\%')
		notify-send -a "Volume" -u low "Volume" -h int:value:$value
		;;
	mute)
		amixer -q set Master toggle
		value=$(amixer get Master | grep -oP '(\[on\]|\[off\])')
		case $value in
			"[on]")
			notify-send -a "Volume" -u low "Volume" "Unmuted"
			;;
			"[off]")
			notify-send -a "Volume" -u low "Volume" "Muted"
			;;
		esac

esac
