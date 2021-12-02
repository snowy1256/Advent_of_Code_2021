INPUT_ARRAY = []

def parse_input_file(fpath="day1_input.txt"):
    with open(fpath, 'r') as f:
        for input in f:
            INPUT_ARRAY.append(input)

def get_num_increments():
    num_increments = 0
    for i in range(len(INPUT_ARRAY)):
        if i == 0:
            continue
        curr_input = int(INPUT_ARRAY[i])
        prev_input = int(INPUT_ARRAY[i - 1])
        if prev_input < curr_input:
            num_increments += 1
    print num_increments


if __name__ == "__main__":
    parse_input_file()
    get_num_increments()
