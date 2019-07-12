import sys
import os
import socket
import json

encodings = ['unicode', 'utf-8']

dir = input("dir: ")
if sys.platform == 'win32':
    HOST = socket.gethostbyname(socket.gethostname())
else:
    HOST = input("HOST: ")
PORT = 3702

sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender.bind((HOST, PORT))
sender.listen(1)

conn, addr = sender.accept()

paths = [path.replace(dir, '.') for sub in [[os.path.join(w[0], file) for file in w[2]] for w in os.walk(dir)] for path in sub]

conn.send(str(len(paths)).encode())

files = {}
for path in paths:
    files[path] = open(path, 'r').read()

for file in files:
    chunk = [file, files[file]]
    print(sys.getsizeof(file), sys.getsizeof(files[file]))

with open('..\\test.txt', 'w') as f:
    f.write(json.dumps(files, indent=4, sort_keys=True))
