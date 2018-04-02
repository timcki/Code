#include <stdlib.h>
#include <stdio.h>
#include <ncurses.h>

int randr(int min, int max) {
    int rv = 0;
    do {
        rv = rand() % max;
        printf("rv: %d", rv);
        getchar();
    } while (rv <= min);
    return rv;
}

int main() {
    int x, y;
    getmaxyx(initscr(), y, x);
    printf("y: %d, x:%d\n", y, x);
    return 0;
}

