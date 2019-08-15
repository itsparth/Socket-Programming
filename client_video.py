import os
from socket import *
import cv2
import numpy as np
import pickle

host = "127.0.0.1"
port = 8000

sock = socket()
sock.connect((host, port))

cap = cv2.VideoCapture(0)

ret, frame  = cap.read()
data_string = pickle.dumps(frame)
sock.send(data_string)

while True:
    ret, frame  = cap.read()
    data_string = pickle.dumps(frame)
    sock.send('@#@'.encode() + data_string)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
sock.close()
os._exit(0)