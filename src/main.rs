#![allow(unused_imports)]

use std::net::{TcpListener, TcpStream};
use std::env;
use std::process::exit;

const TOR_SERVER: &str = "127.0.0.1";
const TOR_SERVER_CONTROL_PORT: u16 = 9051;
const TOR_SERVER_SOCKS_PORT: u16 = 9050;

fn main() {
    let argv: Vec<String> = env::args().collect();
    let argc: usize = argv.len();
    if argc <= 1 { exit(-1); }

    let running: bool = true;

    println!("Argument: {}", argv[1]);

    // start program loop
    loop {
        if !running { break; }

        //establish a connection to the tor control node
        // connect_node(TOR_SERVER);
    }
}
