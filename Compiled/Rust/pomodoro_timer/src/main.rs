//#[macro_use]
//extern crate serde_derive;
//extern crate csv;
extern crate time;

//mod pomodoro;
mod timer;
mod prompts;

const SESSION_TIME:     i32     = 1500;
const SHORT_BREAK_TIME: i32     = 300;
const LONG_BREAK_TIME:  i32     = 1800;

fn main() {
    let mut next_session: i32;
    loop {
        match prompts::break_prompt() {
            prompts::TimerType::ShortBreak => next_session = SHORT_BREAK_TIME,
            prompts::TimerType::LongBreak => next_session = LONG_BREAK_TIME,
            prompts::TimerType::Pomodoro => next_session = SESSION_TIME,
            prompts::TimerType::Quit => std::process::exit(1)
        }
        let (handle, timer) = timer::PomodoroTimer::start_timer(next_session);
        loop {
            match timer.receiver.recv() {
                Err(_) => break,
                Ok(time) => prompts::print_progress_bar(time.as_secs() as f32, next_session as f32, '█')
            }
        }
        handle.join().unwrap();
    }
}
