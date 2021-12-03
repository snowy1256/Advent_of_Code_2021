INPUT_ARRAY = []

def parse_input():
    with open("day2_input.txt") as f:
        for input in f:
            instruction = input.split(" ")
            INPUT_ARRAY.append(instruction)


def steer_submarine():
    submarine_position = [0, 0]
    aim = 0
    for direction, distance in INPUT_ARRAY:
        if direction == "forward":
            submarine_position[0] += int(distance)
            if aim != 0:
                submarine_position[1] += (aim * int(distance))
        if direction == "down":
            aim += int(distance)
        if direction == "up":
            aim -= int(distance)
    return submarine_position

def mult_position(sub_pos):
    print(sub_pos[0] * sub_pos[1])

if __name__ == "__main__":
    parse_input()
    sub_pos = steer_submarine()
    mult_position(sub_pos)