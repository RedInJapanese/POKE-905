use std::io::Read;
use std::fs::File;

fn main(){
    let mut file = File::open("rgb.txt").expect("Error. Unable to open file.");
    let mut contents = String::new();

    file.read_to_string(&mut contents).expect("Error. Unable to read file.");
    println!("Contents:\n {}", contents)
}