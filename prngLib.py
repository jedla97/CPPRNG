import matplotlib.pyplot as plt


# formula for generate random number
def prng(seed):
    x = seed_value(seed)
    a = 1664525
    c = 1013904223
    m = 2 ** 32
    x = (a * x + c) % m
    return x


# decrease value of seed because seed must be lower then modulo m in formula
def seed_value(value):
    if value > (2 ** 32):
        value = value / 10
        seed_value(value)

    else:
        return int(value)
    return int(value)


# controlling when is number in rage
def in_range(range_min, range_max, number):
    if range_min <= number < range_max:
        return number
    elif number > range_max:
        return -2  # for number get above target range
    else:
        return -1  # for number not in range


# modulo of some number
def modulo_of_input(number, limit):
    if number <= limit:
        return number
    else:
        return number % limit


# edits value of generate numbers by its range
# by controlling range_min make sure not to divide by 0
# all state for function are probably done #notSure
def range_of_generate_number(range_min, range_max, rngNumber):
    counter = 0  # for number of iteration don't increase above difference of range_max - range_min
    number = 0  # returned final number in range
    if range_min == 0:  # minimum is 0 so lower range doesn't matter
        number = modulo_of_input(rngNumber, range_max)
        return number
    elif range_min == 1:  # not sure if this is needed maybe duplicated with code in else
        number_of_max = modulo_of_input(rngNumber, range_max)
        if number_of_max == 0:
            while True:
                if counter == (range_max - range_min - 1):
                    counter = 0
                number_of_min = modulo_of_input(rngNumber, range_min + counter)
                number = number + number_of_min
                help_return = in_range(range_min, range_max, number)
                if help_return == -1:
                    counter = counter + 1
                elif help_return == -2:
                    number = modulo_of_input(number, range_max)
                    help_return = in_range(range_min, range_max, number)
                    if help_return >= 0:
                        return number
                else:
                    return number
        else:
            number = number_of_max
            while True:
                if counter == (range_max - range_min - 1):
                    counter = 0
                help_return = in_range(range_min, range_max, number)
                if help_return == -1:
                    number_of_min = modulo_of_input(rngNumber, range_min + counter)
                    number = number + number_of_min
                    counter = counter + 1
                elif help_return == -2:
                    number = modulo_of_input(number, range_max)
                else:
                    return number
    else:  # for every other min than 0 and 1
        number_max = modulo_of_input(rngNumber, range_max)
        if number_max == 0:
            while True:
                if counter == (range_max - range_min - 1):
                    counter = 0
                number_min = modulo_of_input(rngNumber, range_min + counter)
                number = number + number_min
                help_range = in_range(range_min, range_max, number)
                if help_range == -1:
                    counter = counter + 1
                elif help_range == -2:
                    number = modulo_of_input(number, range_max)
                    help_range = in_range(range_min, range_max, number)
                    if help_range >= 0:
                        return number
                else:
                    return number
        else:
            number = number_max
            while True:
                if counter == (range_max - range_min - 1):
                    counter = 0
                number_min = modulo_of_input(rngNumber, range_min + counter)
                number = number + number_min
                help_range = in_range(range_min, range_max, number)
                if help_range == -1:
                    counter = counter + 1
                elif help_range == -2:
                    number = modulo_of_input(number, range_max)
                    help_range = in_range(range_min, range_max, number)
                    if help_range >= 0:
                        return number
                else:
                    return number


# for generate multiple numbers return array of numbers
def multiple_numbers(iteration, seed):
    x = seed
    i = 0
    y = []
    while i < iteration:
        x = prng(x)
        # print(range_of_generate_number(1000000001, 1000000009, x))
        y.append(x)
        i += 1
    return y


# plotting the graph
def plot_numbers(arr):
    plt.plot(arr, 'o')
    plt.show()
