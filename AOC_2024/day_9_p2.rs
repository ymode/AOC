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
                    disk.extend(std::iter::repeat(Some(id)).take(block.length));
                }
            }
            BlockType::Free => {
                disk.extend(std::iter::repeat(None).take(block.length));
            }
        }
    }
    disk
}

#[derive(Clone, Debug)]
struct FileInfo {
    id: usize,
    start: usize,
    length: usize,
}

fn compact_disk_whole_files(disk: &mut Vec<Option<usize>>) {
    use std::collections::HashMap;
    let mut file_data: HashMap<usize, FileInfo> = HashMap::new();

    // Gather file positions
    for (idx, &maybe_id) in disk.iter().enumerate() {
        if let Some(fid) = maybe_id {
            file_data
                .entry(fid)
                .and_modify(|info| {
                    info.length += 1;
                    if idx < info.start {
                        info.start = idx;
                    }
                })
                .or_insert(FileInfo {
                    id: fid,
                    start: idx,
                    length: 1,
                });
        }
    }

    // Sort files by descending ID
    let mut files: Vec<FileInfo> = file_data.into_values().collect();
    files.sort_by(|a, b| b.id.cmp(&a.id));

    // Attempt to move each file exactly once
    for file in files {
        if file.length == 0 {
            continue;
        }

        if let Some(free_run_start) = find_leftmost_free_run(disk, file.start, file.length) {
            move_whole_file(disk, file.id, free_run_start, file.length);
        }
    }
}

fn find_leftmost_free_run(
    disk: &[Option<usize>],
    max_index: usize,
    run_length: usize
) -> Option<usize> {
    let mut i = 0;
    // Only search [0 .. max_index) because we only want to move "to the left of file.start"
    while i + run_length <= max_index {
        let slice = &disk[i .. (i + run_length)];
        if slice.iter().all(|b| b.is_none()) {
            return Some(i);
        }
        i += 1;
    }
    None
}

fn move_whole_file(
    disk: &mut Vec<Option<usize>>,
    file_id: usize,
    dest_start: usize,
    length: usize
) {
    // Clear the old blocks
    for block in disk.iter_mut() {
        if *block == Some(file_id) {
            *block = None;
        }
    }

    // Place file_id in the destination range
    for idx in dest_start .. dest_start + length {
        disk[idx] = Some(file_id);
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

    // Perform PART TWO (whole-file) compaction:
    compact_disk_whole_files(&mut disk);

    let checksum = calculate_checksum(&disk);
    println!("The resulting filesystem checksum is: {}", checksum);
}
