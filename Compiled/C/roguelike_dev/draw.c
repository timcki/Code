#include <ncurses.h>
#include "draw.h"
#include "game_types.h"

int screen_setup() {
    initscr();
    noecho();
    refresh();
    return 0;
}


// When it was a first draft it only printed the whole map cell by cell now i want to add some camera movement based on where the player is.
// TODO
int map_draw(Player *player, Map *map) {
    for (int y=0;y<100;y++) {
        for (int x=0;x<100;x++) {
            switch (map->tile[y][x]) {
                case Floor:
                    mvprintw(y, x, ".");
                    break;

                case Wall:
                    mvprintw(y,x,"#");
                    break;

                default:
                    break;
            }
        }
    }
    mvprintw(player->position.y, player->position.x, "@");
    refresh();
    return 0;
}

int player_move(Position new_position, Player *player, Map *map) {

    // Check for colision first
    if (map->tile[new_position.y][new_position.x] != Wall) {


        // Update player position
        player->position.y = new_position.y;
        player->position.x = new_position.x;

        return 0;
    }
    else return 1;
}
