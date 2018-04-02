use time;
use std::sync::mpsc::Receiver;
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

pub struct PomodoroTimer {
    pub receiver:   Receiver<Duration>,
    start_time:     time::Timespec,
    end_time:       Option<time::Timespec>,
}


impl PomodoroTimer {
    
    pub fn start_timer(session_length: i32) -> (thread::JoinHandle<()>, PomodoroTimer) {
        let (tx, rx) = mpsc::channel();
        let handle = thread::spawn(move || {

            let mut pomodoro_time = Duration::from_secs(session_length as u64);
            let sleep_amount = Duration::from_secs(1);

            for x in 0..session_length+1 {
                thread::sleep(sleep_amount);
                tx.send(pomodoro_time).unwrap();
                if x != session_length { pomodoro_time -= sleep_amount; }
            }
        });

        (handle, PomodoroTimer { receiver: rx, start_time: time::get_time(), end_time: None })
    }
}
/*
    pub fn start_short_break_timer() -> (thread::JoinHandle<()>, PomodoroTimer) {
        let (tx, rx) = mpsc::channel();
        let handle = thread::spawn(move || {

            let mut pomodoro_time = Duration::from_secs(SHORT_BREAK_TIME as u64);
            let sleep_amount = Duration::from_secs(1);

            for x in 0..SHORT_BREAK_TIME+1 {
                thread::sleep(sleep_amount);
                tx.send(pomodoro_time).unwrap();
                if x != SHORT_BREAK_TIME { pomodoro_time -= sleep_amount; }
            }
        });

        (handle, PomodoroTimer { receiver: rx, start_time: time::get_time(), end_time: None })
    }

    pub fn start_long_break_timer() -> (thread::JoinHandle<()>, PomodoroTimer) {
        let (tx, rx) = mpsc::channel();
        let handle = thread::spawn(move || {

            let mut pomodoro_time = Duration::from_secs(LONG_BREAK_TIME as u64);
            let sleep_amount = Duration::from_secs(1);

            for x in 0..LONG_BREAK_TIME+1 {
                thread::sleep(sleep_amount);
                tx.send(pomodoro_time).unwrap();
                if x != LONG_BREAK_TIME { pomodoro_time -= sleep_amount; }
            }
        });

        (handle, PomodoroTimer { receiver: rx, start_time: time::get_time(), end_time: None })
    }
*/
