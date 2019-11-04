import seedGen as Gn
import prngLib as Rng

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
number2 = Gn.str_input()
print("test str ", number)
number1 = Gn.user_input()
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
exit(0)
