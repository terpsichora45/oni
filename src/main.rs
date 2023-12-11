#![allow(unused_imports)]

use std::net::{TcpListener, TcpStream};
use std::env;
use std::process::exit;

fn main() {
    let argv: Vec<String> = env::args().collect();
    let argc: usize = argv.len();
    if argc <= 1 { exit(-1); }

    println!("Argument: {}", argv[1]);
}
