/*
 * Text based game about "Pan Tadeusz"
 *
 * Question folder is written with this syntax:
 *  $(index as int)#Question{
 *      @answer(question text, next question index)
 *      @answer(question text, next question index)
 *      @answer(question text, next question index)
 *      @answer(question text, next question index)
 *  }
 *
 */
extern crate pancurses;

mod file_parser;
mod game_elements;

static PATH: &'static str = "/Users/ft3/Dropbox/Code/Rust/game_dev/gra_na_polski/guwno";

fn main() {
    let vector = file_parser::read_file(PATH);
    let questions = file_parser::parse_parameters(vector);
    game_elements::ncurses_elements::game_loop(questions);
    println!("Welcome to pan Tadeusz");
}


