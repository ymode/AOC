use std::fs;

#[derive(Debug)]
enum BlockType {
    File,
    Free,
}

#[derive(Debug)]
struct ParsedBlock {
    block_type: BlockType,
    length: usize,
    file_id: Option<usize>,
}

fn parse_input(input_string: &str) -> Vec<ParsedBlock> {
    let lengths: Vec<usize> = input_string
        .chars()
        .filter_map(|c| c.to_digit(10))
        .map(|d| d as usize)
        .collect();

    let mut parsed = Vec::new();
    let mut file_id = 0;
    let mut is_file = true;
    for length in lengths {
        if is_file {
            parsed.push(ParsedBlock {
                block_type: BlockType::File,
                length,
                file_id: Some(file_id),
            });
            file_id += 1;
        } else {
            parsed.push(ParsedBlock {
                block_type: BlockType::Free,
                length,
                file_id: None,
            });
        }
        is_file = !is_file;
    }
    parsed
}

fn initialize_disk(parsed_input: &[ParsedBlock]) -> Vec<Option<usize>> {
    let mut disk = Vec::new();
    for block in parsed_input {
        match block.block_type {
            BlockType::File => {
                if let Some(id) = block.file_id {
                    // Put 'id' in each block
                    disk.extend(std::iter::repeat(Some(id)).take(block.length));
                }
            }
            BlockType::Free => {
                // Put None in each block
                disk.extend(std::iter::repeat(None).take(block.length));
            }
        }
    }
    disk
}

fn compact_disk(disk: &mut Vec<Option<usize>>) {
    loop {
        let mut moved = false;
        let last_file_index = disk.iter().rposition(|&c| c.is_some());
        let first_free_index = disk.iter().position(|&c| c.is_none());

        if let (Some(free_i), Some(file_i)) = (first_free_index, last_file_index) {
            if file_i > free_i {
                disk.swap(free_i, file_i);
                moved = true;
            }
        }

        if !moved {
            break;
        }
    }
}

fn calculate_checksum(disk: &[Option<usize>]) -> usize {
    disk.iter()
        .enumerate()
        .filter_map(|(i, &maybe_id)| {
            if let Some(id) = maybe_id {
                Some(i * id)
            } else {
                None
            }
        })
        .sum()
}

fn main() {
    let disk_map_str = fs::read_to_string("day_9.txt").expect("Unable to read file");
    let parsed_input = parse_input(&disk_map_str);
    let mut disk = initialize_disk(&parsed_input);

    compact_disk(&mut disk);
    let checksum = calculate_checksum(&disk);

    println!("The resulting filesystem checksum is: {}", checksum);
}
