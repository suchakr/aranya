import RPi.GPIO as GPIO
import socket
from time import time, sleep
import json
import os

# Create and configure logger
import logging
logging.basicConfig(filename="./shrona.log", format='%(asctime)s %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Utility class to keep track of elapsed time
class TimeKeeper:
    def __init__(self):
        self.start_time = time()
        self.last_time = self.start_time
        self.elapsed_time = [0, 0]

    def elapsed(self):
        now = time()
        self.elapsed_time[0] = now - self.last_time
        self.elapsed_time[1] = now - self.start_time
        self.last_time = now
        return self

    def __str__(self):
        et = self.elapsed_time
        return f"{et[0]:.2f}s, {et[1]:.2f}"

    def test():
        tk = TimeKeeper()
        for i in range(10):
            print(tk.elapsed())
            sleep(.5)
tk = TimeKeeper()

# Main - SHRONA श्रोण hear
SHRONA_DEVICE_ID = os.environ.get('SHRONA_DEVICE_ID', socket.gethostname())
CHANNEL = int(os.environ.get('SHRONA_GPIO_CHANNEL', 17))
UDP_PORT = int(os.environ.get('TRIKONATE_PORT', 5005))
UDP_IP = os.environ.get(
    'TRIKONATE_IP',
    socket.gethostbyname_ex(socket.gethostname())[-1][-1]
)

GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.IN)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

def callback(channel):
    tick = time()
    global sock
    g = GPIO.input(channel)
    sound_event = {'device_id': SHRONA_DEVICE_ID, 'time': tick, 'level': g}
    sound_json = json.dumps(sound_event)
    sock.sendto(bytes(sound_json, 'ascii'), (UDP_IP, UDP_PORT))

    global tk
    tk.elapsed()
    sound_event['elapsed'] = str(tk)
    info =  json.dumps(sound_event)
    logger.info(info)

GPIO.add_event_detect(CHANNEL, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(CHANNEL, callback)

print("Listening for sound at GPIO %s:%s" % (SHRONA_DEVICE_ID, CHANNEL))
print("Sending to %s:%s" % (UDP_IP, UDP_PORT))
while True:
    sleep(.3)
