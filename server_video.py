import os
from socket import *
import cv2
import numpy as np
import pickle

host = "0.0.0.0"
port = 8000

sock = socket()
sock.bind((host, port))
sock.listen(2)

total = bytes()
sc, addr = sock.accept()
while True:
    data = sc.recv(1024)
    s_data = data.split('@#@'.encode())
    if len(s_data) > 1:
        frame = pickle.loads(total + s_data[0])
        cv2.imshow('stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        total = s_data[1]
    else:
        total += data
sock.close()
os._exit(0)