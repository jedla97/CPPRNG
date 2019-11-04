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


def range_of_generate_number(int1, int2, rngNumber):
    if int1 < 10 and int2 < 10:
        return int(rngNumber / 1000000000)
    elif (10 <= int1 < 100) and (10 <= int2 < 100):
        return int(rngNumber / 100000000)
    elif (100 <= int1 < 1000) and (100 <= int2 < 1000):
        return int(rngNumber / 10000000)
    elif (1000 <= int1 < 10000) and (1000 <= int2 < 10000):
        return int(rngNumber / 1000000)
    elif (10000 <= int1 < 100000) and (10000 <= int2 < 100000):
        return int(rngNumber / 100000)
    elif (100000 <= int1 < 1000000) and (100000 <= int2 < 1000000):
        return int(rngNumber / 10000)
    elif (1000000 <= int1 < 10000000) and (1000000 <= int2 < 10000000):
        return int(rngNumber / 1000)
    elif (10000000 <= int1 < 100000000) and (10000000 <= int2 < 100000000):
        return int(rngNumber / 100)
    elif (100000000 <= int1 < 1000000000) and (100000000 <= int2 < 1000000000):
        return int(rngNumber / 10)
    elif (1000000000 <= int1 < 10000000000) and (1000000000 <= int2 < 10000000000):
        return int(rngNumber / 1)
    else:
        print("will be edited later")  # TO-DO
        return int(rngNumber)
