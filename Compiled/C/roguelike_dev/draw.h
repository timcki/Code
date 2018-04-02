#ifndef draw_h_INCLUDED
#define draw_h_INCLUDED

#include "game_types.h"

int screen_setup();
Map * map_setup();
int player_move(Position new_position, Player *player, Map *map);
int map_draw(Player *player, Map *map);

#endif // draw_h_INCLUDED

