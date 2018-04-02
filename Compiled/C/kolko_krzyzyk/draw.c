#include <ncurses.h>
#include "draw.h"

int
init_window(void) {
	initscr();
	noecho();
	return 0;
}
