#include "game_types.h"
#include <math.h>
#include <ncurses.h>

#define NUMBER_OF_TRIES 200

#define MIN_COORD 10
#define MAX_COORD 40

#define MIN_ROOM 4
#define MAX_ROOM 10

// Generates random value in range between min and max
int randr(int min, int max) {
    int rv = 0;
    do {
        rv = rand() % max;
    } while (rv <= min);
    return rv;
}

int check_collision(Map *map, int y, int x, int y_size, int x_size) {
    // Check if any of the cells collide instead of just corners like before, because it caused to many collisions
        for (int i=y; i <= y + y_size; i++)
            for (int j=x; j <= x + x_size; j++)
                if (map->tile[i][j] != None) return 0;
         return 1;

        //&& map->tile[y+y_size][x] == None
        //&& map->tile[y][x+x_size] == None
        //&& map->tile[y+y_size][x+x_size] == None) return 1;
}

Map *map_setup() {
    Map *map;

    map = (Map *)malloc(sizeof(Map));

    for (int y=0;y<100;y++) {
        for (int x=0;x<100;x++) {
            map->tile[y][x] = None;
        }
    }

    //Before starting to randominze numbers change seed
    srand(getch());

    // Try NUMBER_OF_TRIES times to place a room without intersecting with another
    for (int t=0; t < NUMBER_OF_TRIES; t++) {
        int y = randr(MIN_COORD, MAX_COORD);
        int x = randr(MIN_COORD, MAX_COORD);

        int y_size = randr(MIN_ROOM, MAX_ROOM);
        int x_size = randr(MIN_ROOM, MAX_ROOM);

        // Check if any of the corners end up in another room
        if (check_collision(map, y, x, y_size, x_size)) {

            // Fill the vertical walls first then do the same for horizontal ones
            // Added y+ and x+ in the i<= section of for. Forgot about it shit really important tho
            for (int i=y; i<=y+y_size; i++) {
                map->tile[i][x] = Wall;
                map-> tile[i][x+x_size] = Wall;
            }

            for (int i=x; i<=x+x_size; i++) {
                map->tile[y][i] = Wall;
                map-> tile[y+y_size][i] = Wall;
            }

            for (int i=y+1; i <= y + y_size-1; i++) {
                for (int j=x+1; j <= x + x_size-1; j++) {
                    map->tile[i][j] = Floor;
                }
            }
        }
    }

    return map;
}

