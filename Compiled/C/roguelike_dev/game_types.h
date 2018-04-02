#ifndef game_types_h_INCLUDED
#define game_types_h_INCLUDED

//Wrapper around the position to have it under one place
typedef struct {
    int x;
    int y;
} Position;

typedef enum {
    None,
    Wall,
    Floor,
} TileType;

//typedef struct {
    //char name[20];
//} Item;

typedef struct { 
    TileType tile[100][100];
    Position camera_position;
    } Map;

typedef struct {
    Position position;
    int health;
} Player;

#endif // game_types_h_INCLUDED

