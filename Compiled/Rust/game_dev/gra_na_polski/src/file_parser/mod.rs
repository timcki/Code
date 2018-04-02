use std::io::{BufReader, BufRead};
use std::fs::File;
use game_elements;

enum TextType {
    Question,
    Answer,
    Index
}


pub fn read_file(path: &str) -> Vec<String> {
    let f = File::open(path).unwrap();
    let file = BufReader::new(&f);
    let mut buffer = String::new();
    
    for line in file.lines() {
        buffer += line.unwrap().as_str();
        buffer += "\n";
    } 

    buffer.split("}").map(|x| x.to_string()).collect()
}


pub fn parse_parameters(questions: Vec<String>) -> Vec<game_elements::Question> {
    let mut current_state = TextType::Index;
    let mut questions_vector = (0..150).map(|_| game_elements::make_dummy_question()).collect::<Vec<game_elements::Question>>();
    for question in questions {

        // println!("=+=+=>> {}", question);
        let mut index = String::new();
        let mut q_index: usize = 0; 
        let mut a_index = Vec::new();
        let mut question_text = String::new();
        let mut answer = String::new();
        let mut vec_answers = Vec::new();

        for chars in  question.chars().skip(2) {
            match current_state {
                TextType::Index => {
                    match chars {
                        '\n' => {},
                        '{' => {},
                        '$' => {},
                        '#' => { 
                                    current_state = TextType::Question;
                                    q_index = index.trim().parse::<usize>().unwrap();
                                    index = String::new();
                                },
                        '@' => {
                                    current_state = TextType::Answer;
                                    vec_answers.push(answer);
                                    answer = String::new();
                                    a_index.push(index.trim().parse::<usize>().unwrap());
                                    index = String::new();
                                },
                        _   => { index += chars.to_string().trim() }
                    }
                },

                TextType::Question => {
                    match chars {
                        '{' => {},
                        '@' => { current_state = TextType::Answer },
                        '$' => { current_state = TextType::Index },
                        _   => { question_text += chars.to_string().as_str() }
                    }
                },

                TextType::Answer => {
                    match chars {
                        '$' => { current_state = TextType::Index },
                        _   => { answer += chars.to_string().as_str() }
                    }
                }
            }
        
        }
            // println!("qi:{}", q_index);
            // println!("ai:{:?}", a_index);
            // println!("{}", question_text);
            // println!("{:?}", vec_answers);
            let res_vec = vec_answers.into_iter().zip(a_index).collect::<Vec<(String, usize)>>();
            let q = game_elements::Question::new(q_index, question_text, game_elements::new_vec(res_vec));
            let tmp_index = q.index;
            questions_vector[tmp_index] =  q;
            current_state = TextType::Index;
    }
    questions_vector
}


