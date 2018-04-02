struct Player {
    name: &str,
    equipment: Vec<Item>,
    statistics: Statistics,
    position: Coordinates
}


enum Item {
    Potion { name: &str, description: &str },
    Weapon { name: &str, description: &str },
    Food { name: &str, description: &str },
    Other { name: &str, description: &str }
}


struct Statistics {
    health: i32,
    armor: i32,
    mana: i32,
    ad: i32,
    ap: i32
}


struct Coordinates {
    x: usize,
    y: usize
}
