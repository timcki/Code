use pancurses::{initscr, endwin, noecho};
use game_elements::*;

static COLOR_BACKGROUND: i16 = 16;
static COLOR_ANSWER: i16 = 17;
static COLOR_QUESTION: i16 = 18;

static COLOR_PAIR_DEFAULT: i16 = 1;
static COLOR_PAIR_QUESTION: i16 = 2;

trait game_window {
    fn init_screen();
    fn select_choice(question: &Question) -> usize;
    fn print_question(strings: &Vec<String>, qn: usize);

fn init_screen() {
    let window = initscr();
    window.keypad(true);
    curs_set(0);
    noecho();

    start_color();
    init_color(COLOR_BACKGROUND, 0, 43 * 4, 54 * 4);
    init_color(COLOR_QUESTION, 147 * 4, 161 * 4, 161 * 4);
    init_color(COLOR_ANSWER, 133 * 4, 153 * 4, 0);

    init_pair(COLOR_PAIR_DEFAULT, COLOR_ANSWER, COLOR_BACKGROUND);
    init_pair(COLOR_PAIR_QUESTION, COLOR_QUESTION, COLOR_BACKGROUND);
}
    
fn select_choice(question: &Question) -> usize {
    let texts = question.return_all_strings();
    let mut qi: usize = 1;
    print_question(&texts, qi);
    let limit = question.answers_quantity();
    let mut dir = getch();
    while dir != '\n' as i32 {
        match dir {
            KEY_UP      => { if qi > 1 { qi -= 1 } },
            KEY_DOWN    => { if qi < limit { qi += 1 } }
            _           => {}
        }
        print_question(&texts, qi);
        dir = getch();
    }
    question.next_question_index(qi - 1)
}

fn print_question(strings: &Vec<String>, qn: usize) {
    clear();
    mv(10,0);
    printw(strings[0].as_str());
    for (ind, things) in strings.iter().enumerate().skip(1) {
        printw("\n");
        attron(COLOR_PAIR(COLOR_PAIR_DEFAULT));
        if ind==qn {
            attron(A_BOLD() | A_BLINK());
            printw(things.as_str());
            attroff(A_BOLD() | A_BLINK());
        }
        else { 
            printw(things.as_str());
        }
        attroff(COLOR_PAIR(COLOR_PAIR_DEFAULT));
    }
    refresh();
}
    
pub fn game_loop(game_questions: Vec<Question>) {
    let mut current_question: usize = 1;
    let mut game = true;
    init_screen();
    welcome_to_alpha();
    while game {
        if current_question == 138 { game = false; }
        current_question = select_choice(&game_questions[current_question]);
    }
    endwin();
}

fn welcome_to_alpha() {
    mv(20,0);
    attron(A_BOLD());
    printw("Welcome to Pan Tadeusz\n");
    attroff(A_BOLD());
    attron(COLOR_PAIR(COLOR_PAIR_DEFAULT));
    printw("Alpha -0.9\n");
    attroff(COLOR_PAIR(COLOR_PAIR_DEFAULT));
    printw("Press any key to continue...\n");
    getch();
}



