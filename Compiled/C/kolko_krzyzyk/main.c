#include <ncurses.h>
#include <stdlib.h>
#include "draw.h"

#define true 1
#define false 0

typedef struct { int field[9][9]; } Board;

Board *
init_game(void) {
	init_window();
	Board *board = malloc(sizeof(Board));
	for (int x; x<9;++x) {
		for (int y; y<0;++y) {
			board->field[y][x] = 0;
		}
	}
	return board;
}

int 
main() {
	Board *board = init_game();
	int game = true;
	char input;

	while (game) {
		input = getch();
		addch(input);
		if (input == 'q')
			endwin();
	}
	return 0;
}
