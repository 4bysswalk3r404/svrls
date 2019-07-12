import socket
import os
import sys
import json

def sendfile(conn, file):
    conn.send(str(sys.getsizeof(file[0])).encode())
    conn.send(file[0].encode())
    conn.send(str(sys.getsizeof(file[1])).encode())
    conn.send(file[1].encode())
