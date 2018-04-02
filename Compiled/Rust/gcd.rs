use std::io::stdin;

fn main() {
    let mut number_of_times = String::new();
    stdin().read_line(&mut number_of_times).unwrap();

    let number_of_times: usize = number_of_times.trim().parse().unwrap();
    let mut ulameczki: Vec<u32, u32> = vec![(0, 0), number_of_times];
    
    let mut tmp = String::new();
    
    for x in 0..number_of_times {
    	stdin().read_line(&mut tmp).unwrap();
        
    	ulameczki[x] = tmp.trim().split(" ")
    		.map(|x, y| x.parse().unwrap(), y.parse().unwrap())
    		.collect()::<(u32, u32)>
    }
    

    println!("{:?}", ulameczki);
}