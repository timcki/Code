#! /usr/bin/mksh

notify-send -c "Music" "Currently Playing" "$(mpc current -f '[%title%]|[%file%]')"
