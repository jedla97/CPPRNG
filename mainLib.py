import prngLib as Rng
import seedGen as Gn

'''
number = Gn.get_time()
print("test time ", number)
number = Rng.prng(number)
print("random ", number)
number = Gn.free_memory()
print("test memory ", number)
number = Rng.prng(number)
print("random ", number)
number = Gn.audio_average()
print("test audio ", number)
number = Rng.prng(number)
print("random ", number)
number = Rng.range_of_generate_number(4, 8, number)
print("random in range <10 ", number)
number = Gn.cpu_gen_process_time()
print("test cpu ", number)
number = Rng.prng(number)
print("random ", number)
number = Rng.range_of_generate_number(11, 75, number)
print("random in range <100 ", number)
number1 = Gn.user_input()
number2 = Gn.str_input()
print("test str ", number)
print("test user ", number)
number1 = Gn.bin_to_decimal(number1)
print("test user decimal ", number1)
number2 = Gn.bin_to_decimal(number2)
print("test str decimal ", number2)
number = Gn.xor_of_str_input(number1, number2)
print("test xor ", number)
number = Rng.prng(number)
print("random ", number)
number = Rng.range_of_generate_number(110, 750, number)
print("random in range <1000 ", number)
# arr = Rng.multiple_numbers(10000, Gn.audio_average())
# Rng.plot_numbers(arr)
'''


def safe_gen():
    seed1 = generate_audio()
    seed2 = generate_memory()
    seed3 = generate_time()
    seed1 = Gn.xor_of_str_input(seed1, seed2)
    seed1 = Gn.xor_of_str_input(seed1, seed3)
    number = generate_in_range(100, 999, seed1)
    return number


def generate_memory():
    number = Gn.free_memory()
    number = Rng.prng(number)
    return number


# TODO look why it's lagging while generating #fix
def generate_audio():
    number = Gn.audio_average()
    number = Rng.prng(number)
    return number


def generate_time():
    number = Gn.cpu_gen_process_time()
    number = Rng.prng(number)
    return number


def generate_plot(range_min, range_max):
    arr = generate_in_range(range_min, range_max)
    Rng.plot_numbers(arr)


def generate_in_range(range_min, range_max, seed):
    return Rng.range_of_generate_number(range_min, range_max + 1, seed)


# testing function
# TODO add to range_max +1 in final version
def generate_in_range_multiple(range_min, range_max):
    i = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    epsilon = Gn.audio_average()
    ye = Rng.multiple_numbers(100, epsilon)

    for i in ye:
        number = Rng.range_of_generate_number_b(range_min, range_max + 1, i)
        print(number)
        i = i + 1
        if number == 7:
            a = a + 1
        elif number == 8:
            b = b + 1
        elif number == 9:
            c = c + 1
        elif number == 10:
            d = d + 1
        elif number == 11:
            e = e + 1
        elif number == 12:
            f = f + 1
        elif number == 13:
            g = g + 1
    print(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + str(e) + " " + str(f) + " " + str(g))
    return ye


def compare_numbers(num1, num2):
    if num1 < num2:
        return 1
    elif num1 > num2:
        return 2
    else:
        return -1
