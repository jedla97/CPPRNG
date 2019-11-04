import random  # used for generate string
import string
import binascii

import pyaudio  # used for generate audio in real time  to install module pip install PyAudio
import numpy as np
import psutil  # used for getting computer statistic    to install module pip install psutil
import time

CHUNK = 4096  # 4096b for audio
RATE = 44100  # bitrate


# generate average from audio chunk which is live recorded
def audio_average():
    p = pyaudio.PyAudio()
    # access to microphone default channel is 1
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    # first chunk is often almost empty chunks so it's used 12 iteration
    for i in range(12):
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        average = np.average(np.abs(data))

    stream.stop_stream()
    stream.close()
    p.terminate()
    return int(average*(2**8))


# access to cpu process time
# generate system for more info documentation( time spend procesing in kernel)
def cpu_gen_process_time():
    info = psutil.cpu_times()
    return int(info[1] * 100000)


# user input as part of entropy
def user_input():
    str_text = input("Type something: ")
    res = bin(int.from_bytes(str_text.encode(), 'big'))
    return res


# generate random string
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
