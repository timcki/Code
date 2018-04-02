use pancurses::{initscr, Window, endwin};

pub fn start_game() {
    let mut window = initscr();
    window.title_screen();
    window.getch();
    endwin();
}

trait GameWindow {
    fn title_screen(&self);
}

impl GameWindow for Window {
    fn title_screen(&self) {
        self.clear();
        let (max_y, max_x) = self.get_max_yx();
        self.m
        self.printw(format!("X: {},\tY: {}", max_x, max_y).as_str());
    }
}
