import os
import socket

from Cryptodome.Cipher import AES

key = b"TheNeuralNineKEy"
nonce = b"TheNeuralNineKey"

cipher = AES.new(key, AES.MODE_EAX, nonce)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

file_size = os.path.getsize("File")

with open(file_size, "rb") as f:
    data = f.read()

encrypted = cipher.encrypt(data)

client.send("File.txt".encode())
client.send(str(file_size).encode())
client.sendall(encrypted)
client.send(b"<END>")

client.close()

