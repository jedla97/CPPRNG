import numpy as np
from numba.utils import bit_length

import prngLib as Rng
import seedGen as Gn

from NIST_statistical_test import monobit_test as mt


# generate seed for safe generate
def seed_for_save_gen():
    seed1 = generate_audio()
    seed2 = generate_memory()
    seed3 = generate_time()
    seed1 = Gn.xor_of_str_input(seed1, seed2)
    seed1 = Gn.xor_of_str_input(seed1, seed3)
    return seed1


# generate number in range 100 - 999 from PRNG
def safe_gen():
    seed = seed_for_save_gen()
    number = generate_in_range(100, 999, seed)
    return number


# generate random number from PRNG with seed from memory
def generate_memory():
    number = Gn.free_memory()
    number = Rng.prng(number)
    return number


# generate random number from PRNG with seed from audio
def generate_audio():
    number = Gn.audio_average()
    number = Rng.prng(number)
    return number


# generate random number from PRNG with seed from Cpu time
def generate_time():
    number = Gn.cpu_gen_process_time()
    number = Rng.prng(number)
    return number


# generate plot for testing by visual from PRNG with one seed
def generate_plot(range_min, range_max, seed):
    arr = generate_in_range_multiple(range_min, range_max, seed)
    Rng.plot_numbers(arr)


# generate plot for testing function
def generate_plot_small(arr):
    Rng.plot_numbers(arr)


# generate number in specific range
def generate_in_range(range_min, range_max, seed):
    return Rng.range_of_generate_number(range_min, range_max + 1, seed)


# generate array from one seed
def generate_in_range_multiple(range_min, range_max, seed):
    numbers = []
    arr = Rng.multiple_numbers(1000, seed)
    for i in arr:
        number = Rng.range_of_generate_number(range_min, range_max + 1, i)
        numbers.append(number)
    return numbers


# comparing two numbers and return only code
def compare_numbers(num1, num2):
    if num1 < num2:
        return 1
    elif num1 > num2:
        return 2
    else:
        return -1


# function for testing approximate entropy
def ApEn(U, m, r) -> float:
    """Approximate_entropy."""

    def _maxdist(x_i, x_j):
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

    def _phi(m):
        x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
        C = [len([1 for x_j in x if _maxdist(x_i, x_j) <= r]) / (N - m + 1.0) for x_i in x]
        return (N - m + 1.0) ** (-1) * sum(np.log(C))

    N = len(U)

    return abs(_phi(m + 1) - _phi(m))


# testing array for mono bit test
def mono_test(arr):
    for i in arr:
        result = mt.test(bin(i), bit_length(i))
        if result[4] != True:
            return False
    return True


# testing approximate entropy
def approx_test(arr):
    result = ApEn(arr, 2, 3)
    if result >= 0.01:
        return True
    else:
        return False

