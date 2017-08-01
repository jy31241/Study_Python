import socket
s = socket.socket()
host = '127.0.0.1'
port = 8080

s.connect((host,port))

print("연결성공")

s.close


