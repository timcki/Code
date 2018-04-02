extern crate mio;

use std::net::SocketAddr;
use mio::tcp::*;
use mio::deprecated::*;

struct WebSocketServer;

impl Handler for WebSocketServer {
    type Timeout = usize;
    type Message = ();
}

fn main() {
  let mut event_loop = EventLoop::new().unwrap();
  let mut handler = WebSocketServer;
  event_loop.run(&mut handler).unwrap();
}
