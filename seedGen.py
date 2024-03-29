import random  # used for generate string #notUsed
import string
import numpy as np
import pyaudio  # used for generate audio in real time  # to install module pip install PyAudio
import psutil  # used for getting computer statistic # to install module pip install psutil


CHUNK = 4096  # 4096b for audio
RATE = 44100  # bitrate


# generate average from audio chunk which is live recorded
def audio_average():
    p = pyaudio.PyAudio()
    # access to microphone default channel is 1
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    # first chunk is often almost empty chunks so it's used 12 iteration
    # close look - in float average have long number so 2 iteration is enough => faster loading
    for i in range(2):
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        average = np.average(np.abs(data))
        # print(average)

    stream.stop_stream()
    stream.close()
    p.terminate()
    return int(average * 10000 * (2 ** 8))


# access to cpu process time
# generate system for more info documentation( time spend processing in kernel)
def cpu_gen_process_time():
    info = psutil.cpu_times()
    return int(info[1] * 100000)


# generate time from clock in in second
# not work on windows so on final build not use
def get_time():
    times = psutil.Process().create_time()
    return int(times)


# generate free memory
def free_memory():
    mem = psutil.virtual_memory()
    return int(mem[1])


# user input as part of entropy
# not use in final build chance of user don't type something so seed == 0
def user_input():
    str_text = input("Type something: ")
    res = bin(int.from_bytes(str_text.encode(), 'big'))
    return res


# generate random string
# do not use not random take numbers from memory
# not use in final build
def str_input():
    letters = string.ascii_letters + string.digits + string.punctuation
    str_text = ''.join(random.choice(letters) for i in range(5))
    res = bin(int.from_bytes(str_text.encode(), 'big'))
    return res


# binary sequence to int
def bin_to_decimal(binary):
    return int(binary, 2)


# xor of two binary string
def xor_of_str_input(binstr1, binstr2):
    ret = binstr1 ^ binstr2
    return int(ret)
