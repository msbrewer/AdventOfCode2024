use std::fs;
use std::collections::HashMap;

fn main() {
    let filename = "input";
    let contents = fs::read_to_string(filename)
        .expect("Failed to read file");
    let lines: Vec<&str> = contents.lines().collect();

    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();
    for line in lines.iter() {
        let cols: Vec<&str> = line.split_whitespace().collect();
        let l: i32 = cols[0].parse().unwrap();
        let r: i32 = cols[1].parse().unwrap();
        left.push(l);
        right.push(r);
    }
    left.sort_unstable();
    right.sort_unstable();
    let mut distance: i32 = 0;
    for (i, &l) in left.iter().enumerate() {
        let d = l - right[i];
        distance += d.abs();
    }
    println!("Total distance: {:?}", distance);

    let mut counts = HashMap::new();
    for &n in right.iter() {
        *counts.entry(n).or_insert(0) += 1;
    }
    let mut sim: i32 = 0;
    for &l in left.iter() {
        sim += l * counts.get(&l).unwrap_or(&0);
    }
    println!("Similarity score: {:?}", sim);
}
