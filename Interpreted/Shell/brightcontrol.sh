#! /usr/bin/mksh

# changed the value to be passed as percentage, so notifications stack up

case $1 in
	up)
		xbacklight +5;;
	down)
		xbacklight -5;;
esac

notify-send -a Brightness -u low "Brighness" -h int:value:$(xbacklight -get)
