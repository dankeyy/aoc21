use std::fs;
use std::collections::HashMap;

type Pair = (char, char);


fn min_max<'a, I>(vals: I) -> (usize, usize)
where
        I: Iterator<Item = &'a usize>,
{
    let mut maximum = std::usize::MIN;
    let mut minimum = std::usize::MAX;

    for &v in vals{
        maximum = maximum.max(v);
        minimum = minimum.min(v);
    }
    return (minimum, maximum)
}


// advances upto the last step, then returns most frequent - least frequent
fn advance_polymer(polymer: &HashMap<Pair, usize>, last_char: char, rules: &HashMap<Pair, char>, steps: usize) -> usize {

    if 0 == steps {
        let mut counter = HashMap::<char, usize>::new();

        for (&(a,_), count) in polymer {
            *counter.entry(a).or_default() += count;
        }
        *counter.entry(last_char).or_default() += 1;

        let (min, max) = min_max(counter.values());

        return max - min;
    }

    let mut next_polymer: HashMap<Pair, usize> = HashMap::new();
    for (&(a,c), count) in polymer {

        let b = rules[&(a,c)];
        *next_polymer.entry((a,b)).or_default() += count;
        *next_polymer.entry((b,c)).or_default() += count;
    }
    advance_polymer(&next_polymer, last_char, &rules, steps-1)
}


fn main() {
    let text = fs::read_to_string("../14.txt").expect("404");
    let (template, pair_insertion) = text.split_once("\n\n").unwrap();
    let last = template.chars().last().unwrap(); // in favor of last char correction

    let mut init_polymer: HashMap<Pair, usize> = HashMap::new();
    let init_bytes = template.as_bytes();
    let mut pair: Pair;

    // initializing first polymer's hashmap
    for i in 0..(init_bytes.len()-1) {
        pair = (init_bytes[i] as char, init_bytes[i+1] as char);
        *init_polymer.entry(pair).or_default() += 1
    }

    // initializing rules
    let rules = pair_insertion.lines()
                              .map(|l| {
                                  let (a, b) = l.split_once(" -> ").unwrap();
                                  let from: Pair = (a.chars().next().unwrap(), a.chars().last().unwrap());//(a.as_bytes()[0] as char, a.as_bytes()[1] as char);
                                  let to = b.chars().next().unwrap();
                                  (from, to)
                              })
                              .collect::<HashMap<Pair,char>>();



    println!("{:?}", advance_polymer(&init_polymer, last, &rules, 40));
}
