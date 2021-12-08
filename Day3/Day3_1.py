import numpy
INPUT_ARRAY = []


def parse_input():
    with open("day3_input.txt") as f:
        INPUT_ARRAY.extend(f.read().splitlines())


# def calculate_gamma(np_array, column_sums):
#     array_shape = np_array.shape
#     half_length = array_shape[0] / 2
#     gamma_values = []
#     for c_sum in column_sums:
#         if c_sum > half_length:
#             gamma_values.append(1)
#         else:
#             gamma_values.append(0)
#     return gamma_values
#
#
# def calculate_epsilon(np_array, column_sums):
#     array_shape = np_array.shape
#     half_length = array_shape[0] / 2
#     epsilon_values = []
#     for c_sum in column_sums:
#         if c_sum < half_length:
#             epsilon_values.append(1)
#         else:
#             epsilon_values.append(0)
#     return epsilon_values
#
#
# def convert_from_binary(values):
#     strings = [str(value) for value in values]
#     joined_string = "".join(strings)
#     integer = int(joined_string, 2)
#     return integer
#
#
# if __name__ == "__main__":
#     parse_input()
#     array_2d = []
#     for input in INPUT_ARRAY:
#         row = map(int, input)
#         array_2d.append(row)
#     np_array = numpy.empty_like(array_2d)
#     column_sums = numpy.sum(np_array, axis=0)
#     gamma_values = calculate_gamma(np_array, column_sums)
#     epsilon_values = calculate_epsilon(np_array, column_sums)
#     gamma_final = convert_from_binary(gamma_values)
#     epsilon_final = convert_from_binary(epsilon_values)
#     print(gamma_final * epsilon_final)


def get_gamma_epsilon(summed_cols, np_array):
    values = {"gamma": [], "epsilon": []}
    max_value = len(np_array)
    for val in summed_cols:
        if val > max_value/2:
            values["gamma"].append(1)
            values["epsilon"].append(0)
        else:
            values["gamma"].append(0)
            values["epsilon"].append(1)
    return values

def get_value_from_binary(binary):
    gamma = binary["gamma"]
    epsilon = binary["epsilon"]
    gamma_binary_strings = [str(integer) for integer in gamma]
    gamma_binary_string = "".join(gamma_binary_strings)
    gamma_int = int(gamma_binary_string, 2)
    epsilon_binary_strings = [str(integer) for integer in epsilon]
    epsilon_binary_string = "".join(epsilon_binary_strings)
    epsilon_int = int(epsilon_binary_string, 2)
    return gamma_int, epsilon_int

if __name__ == "__main__":
    parse_input()
    np_array_width = len(INPUT_ARRAY[0])
    np_array_height = len(INPUT_ARRAY)
    array_2d = []
    for value in INPUT_ARRAY:
        row = map(int, value)
        array_2d.append(row)
    np_array = numpy.asarray(array_2d)
    summed_cols = np_array.sum(axis=0)
    gamma_epsilon_binary = get_gamma_epsilon(summed_cols, np_array)
    gamma_int, epsilon_int = get_value_from_binary(gamma_epsilon_binary)
    print(gamma_int * epsilon_int)






