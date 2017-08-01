import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 8080

s.bind((host, port))

s.listen(100)

c, addr = s.accept()
print('연결이 시작됨', addr)
c.close()

