#! /usr/bin/mksh

# wrapper around spt for convenience. Responsible for easily pausing and showing
# remaining time on top of starting new instances without ones already running

# variables
RED='[0;31m'
GREEN='[0;32m'
COLOUR_OFF='[0m'
CMD="spt"

if [ -z $1 ]
then
	OPTION="t"
elif [ -n $1 ]
then
	OPTION=$1
fi
	
case $OPTION in
	-n|n)
		if [ ! -f /tmp/running_pom ]
		then
			2>/dev/null 1>/dev/null nohup $CMD &
			echo $! | head -n1 > /tmp/running_pom
		else
			notify-send -a "Pomodoro Timer" "Pomodoro Timer" "Error: Pomodoro already running"
		fi
		;;
	-t|t)
		if [ -f /tmp/running_pom ]
		then
			kill -sSIGUSR1 $(cat /tmp/running_pom)
		else
			notify-send -a "Pomodoro Timer" "Pomodoro Timer" "Error: Pomodoro not running"
		fi
		;;
	-p|p)
		if [ -f /tmp/running_pom ]
		then
			kill -sSIGUSR2 $(cat /tmp/running_pom)
		else
			notify-send -a "Pomodoro Timer" "Pomodoro Timer" "Error: Pomodoro not running"
		fi
		;;
	-k|k)
		if [ -f /tmp/running_pom ]
		then
			kill $(cat /tmp/running_pom)
			rm /tmp/running_pom
			notify-send -a "Pomodoro Timer" "Pomodoro Timer" "Ok: Stopped pomodoro"
		else
			notify-send -a "Pomodoro Timer" "Pomodoro Timer" "Error: Pomodoro not running"
		fi
		;;
	*)
		notify-send -a "Pomodoro Timer" "Pomodoro Timer" "Error: UNKOWN OPTION"
		;;
esac
