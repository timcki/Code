pub mod ncurses_elements;

pub struct Question {
    pub index: usize,
    text: String,
    answers: Vec<Response>
}

pub struct Response {
    text: String,
    question_index: usize
}

impl Question {
    pub fn new(i: usize, t: String, a: Vec<Response>) -> Question {
        Question { index: i, text: t, answers: a }
    }

    fn return_all_strings(&self) -> Vec<String> {
       let mut vec = Vec::new();
       vec.push(self.text.clone());
       let mut smth = make_answers_string(&self.answers);
       vec.append(&mut smth);
       vec
    }

    fn answers_quantity(&self) -> usize {
        (self.answers.len()) as usize
    }

    fn next_question_index(&self, ind: usize) -> usize {
        self.answers[ind].question_index
    }

}

impl Response {
   pub fn new(t: String, qi: usize) -> Response {
        Response { text: t, question_index: qi }
    }
}


pub fn new_vec(ve: Vec<(String, usize)>) -> Vec<Response> {
    ve.into_iter().map(|(text, index)| Response::new(text, index)).collect::<Vec<Response>>()
}

pub fn make_dummy_question() -> Question {
    let an1 = Response::new(String::new(), 1);
    let an2 = Response::new(String::new(), 2);
    let an_vec = vec![an1, an2];
    Question::new(0, String::new(), an_vec)
}

fn make_answers_string(vec: &Vec<Response>) -> Vec<String> {
    vec.iter().map(|x| x.text.clone()).collect::<Vec<String>>()
}
