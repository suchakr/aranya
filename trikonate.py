import socket
import os
import json

# Create and configure logger
import logging
logging.basicConfig(filename="./trikonate.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# fetch from environment variables
UDP_PORT = int(os.environ.get('TRIKONATE_PORT', 5005))
UDP_IP = os.environ.get(
    'TRIKONATE_IP', 
    socket.gethostbyname_ex(socket.gethostname())[-1][-1]
)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
msg = "Listening on %s:%s" % (UDP_IP, UDP_PORT)

logger.info("Listening on %s:%s" % (UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    logger.info(data)
    # msg = f"received message: {data} from {addr}"
    # json = json.loads(data)
    # logger.info(json)

