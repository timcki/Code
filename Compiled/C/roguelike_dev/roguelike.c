/* TODO
 * DONE Collision detection
 * STARTED. GOT RANDOM ROOMS. Procedural generation
 */

#include <tcclib.h>

#include "game_types.h"

#include "map_generator.h"
#include "map_generator.c"

#include "draw.h"
#include "draw.c"


int handle_input(char input, Player *player, Map *map);

Player *player_setup();

int main() {
    // Setting up shit
    char ch;

    Player *player;
    Map *map;

    screen_setup();
    map = map_setup();
    player = player_setup();

    // Game loop
    while((ch = getch()) != 'q') {
        handle_input(ch, player, map);
        map_draw(player, map);
    }
    endwin();
    return 0;
}

Player *player_setup() {
    Player *player;
    player = (Player *)malloc(sizeof(Player));

    player->position.x = 14;
    player->position.y = 12;
    player->health = 100;

    return player;
}

int handle_input(char input, Player *player, Map *map) {

    // Handle moving the player icon
    Position new_position;
    switch(input) {
        case 'w':
        case 'W':
            new_position.y = player->position.y - 1;
            new_position.x = player->position.x;
            break;

        case 'a':
        case 'A':
            new_position.y = player->position.y;
            new_position.x = player->position.x - 1;
            break;

        case 's':
        case 'S':
            new_position.y = player->position.y + 1;
            new_position.x = player->position.x;
            break;

        case 'd':
        case 'D':
            new_position.y = player->position.y;
            new_position.x = player->position.x + 1;
            break;

        default:
            new_position.y = player->position.y;
            new_position.x = player->position.x;
            break;
    }   
    player_move(new_position, player, map);
    return 0;
}
