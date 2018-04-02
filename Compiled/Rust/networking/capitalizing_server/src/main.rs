use std::io::{Read, Write, BufReader, BufRead};
use std::net::{TcpListener, TcpStream};

fn main() {
    // Allows to create a connection to the port. pretty obvious stuff i guess.
    let listener = TcpListener::bind("0.0.0.0:5432").unwrap();
    
    // Waits for a connection while blocking the thread ( .accept() ).
    // Upon receiving a connection returns a TcpStream ( rw )
    // The zero is tuple indexing

    for stream in listener.incoming() {
        std::thread::spawn(|| {
            let stream = stream.unwrap().0;
            handle_request(stream);
        }
    }
}

fn handle_request(mut request: TcpStream) {
    
    let mut reader = BufReader::new(request);

    for line in reader.by_ref().lines() {
        if line.unwrap() == "" {
            break;
        }
    }

    send_response(reader.into_inner());
}

fn send_response(mut stream: TcpStream) {

    let response = "HTTP/1.1 200 OK\n\n<html><body>Hello, World!</body></html>";
    stream.write_all(response.as_bytes()).unwrap();
}
