use time;

#[derive(Debug, Serialize, Deserialize)]
pub struct Pomodoro {
    topic: String,
    start_time: Option<String>,
    end_time: Option<String>,
}

impl Pomodoro {

    // Using this struct at the end of a session to write it to a csv file for logging purposes.
    // Using time structs during timing it and then changing it to string to serialize it.
    // Got tired of lifetimes etc, so resorting to the good old way. ->  Change it to string.
    fn new(topic: String, start_time: Option<time::Tm>, end_time: Option<time::Tm>) -> Result<Pomodoro, ()> {
        if let Some(time) = start_time {
            
            if let Some(e_time) = end_time  {
                let s_start_time = Some(format!( "{}", time.ctime() ));
                let s_end_time = Some(format!( "{}", e_time.ctime() ));

                Ok(Pomodoro { topic: topic, start_time: s_start_time, end_time: s_end_time })
            }
            else { Err(()) }

        }
        else { Err(()) }
    }

    pub fn create_example() -> Pomodoro {
        Pomodoro::new("Some test".to_owned(), Some(time::now()), Some(time::now())).unwrap()
    }



}
