use std::io;
use std::io::{Read, Write};

pub enum TimerType {
    ShortBreak,
    LongBreak,
    Pomodoro,
    Quit
}

// Prints the progress bar with remaining time etc
pub fn print_progress_bar(current: f32, total: f32, fill: char) {
    let percent = 100.0 - (current / total) * 100.0;
    let filled_length = percent as i32;
    let minutes = (current / 60.0) as i32;
    let seconds = current % 60.0;
    print!("\rProgress: {}:{:02} |", minutes, seconds);
    for _ in 0..filled_length { print!("{}", fill); }
    for _ in 0..100-filled_length { print!("-"); }
    print!("| {:.*}% complete\r", 1, percent);
    io::stdout().flush().unwrap();
}

pub fn break_prompt() -> TimerType {
    loop {
        print!("\n\nPomodoro finished. Start new pomodoro(p), short break(b), long break(B) or finish(q): ");
        io::stdout().flush().unwrap();
        let mut character = [0];
        io::stdin().read_exact(&mut character).unwrap();
        match character[0] {
            b'b' => return TimerType::ShortBreak,
            b'B' => return TimerType::LongBreak,
            b'q' => return TimerType::Quit,
            b'p' => return TimerType::Pomodoro,
            _   => continue
        }
    }
}
