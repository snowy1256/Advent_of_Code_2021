INPUT_ARRAY = []

def parse_input_file(fpath="day1_input.txt"):
    with open(fpath, 'r') as f:
        for input in f:
            INPUT_ARRAY.append(int(input))

def get_num_increments():
    num_increments = 0
    for i in range(len(INPUT_ARRAY)):
        if i == 0:
            continue
        curr_input = INPUT_ARRAY[i]
        prev_input = INPUT_ARRAY[i - 1]
        if prev_input < curr_input:
            num_increments += 1
    print(num_increments)

def get_num_increments_sliding_windows():
    sliding_windows = get_sliding_windows()
    num_increments = 0
    for i in range(len(sliding_windows)):
        if i == 0:
            continue
        curr_input = sum(sliding_windows[i])
        prev_input = sum(sliding_windows[i - 1])
        if prev_input < curr_input:
            num_increments += 1
    print(num_increments)


def get_sliding_window(curr_location):
    end_of_sliding_window = curr_location + 2
    if end_of_sliding_window > len(INPUT_ARRAY):
        return None
    sliding_window = INPUT_ARRAY[curr_location:end_of_sliding_window+1]
    return sliding_window


def get_sliding_windows():
    sliding_windows = []
    for i in range(len(INPUT_ARRAY)):
        sliding_window = get_sliding_window(i)
        if sliding_window != None:
            sliding_windows.append(sliding_window)
        else:
            break
    return sliding_windows
    

if __name__ == "__main__":
    parse_input_file()
    get_num_increments_sliding_windows()
