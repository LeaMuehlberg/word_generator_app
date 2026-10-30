use std::env;
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();
    let code: i32 = args[1].parse().unwrap();

    process::exit(code);
}