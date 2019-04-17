import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(input_list=[]):
    if len(input_list) == 1:
        return input_list

    for index in range(0, len(input_list) - 1):
        random_index = get_random(index+1, len(input_list)-1)
        input_list[index], input_list[random_index] = \
            input_list[random_index], input_list[index]

    return input_list


if __name__ == "__main__":
    print(shuffle([1, 2, 3, 4, 5]))