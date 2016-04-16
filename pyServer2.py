
import socket
import sys
import RPi.GPIO as io
import time
io.setmode(io.BOARD)

enL = 11
dL1 = 13
dL2 = 15

enR = 8
dR1 = 10
dR2 = 12

io.setup(enL, io.OUT)
io.setup(dL1, io.OUT)
io.setup(dL2, io.OUT)

io.setup(enR, io.OUT)
io.setup(dR1, io.OUT)
io.setup(dR2, io.OUT)

pL = io.PWM(enL, 500)
pR = io.PWM(enR, 500)


#HOST = '139.78.71.3'	# Symbolic name meaning all available interfaces
#HOST = '127.0.0.1'
HOST = '192.168.15.199'
PORT = 40008	# Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Socket created'

try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	
print 'Socket bind complete'

#s.listen(10)
print 'Socket now listening'

#conn, addr = s.accept()

#print 'Connected with ' + addr[0] + ':' + str(addr[1])
#if(not(s.recvfrom(1024) is None)):
#	s.sendto("Connected",("139.78.71.167",40007))

#now keep talking with the client
while True :
    #wait to accept a connection - blocking call
	
	
	data,addr = s.recvfrom(1024)
	
	print(data)

        direction = data


        if direction == "w":
                io.output(dL1, True)
                io.output(dL2, False)
                io.output(dR1, True)
                io.output(dR2, False)
                pL.start(100)
                pR.start(100)
        elif direction == "s":
                io.output(dL1, False)
                io.output(dL2, True)
                io.output(dR1, False)
                io.output(dR2, True)
                pL.start(100)
                pR.start(100)
	elif direction == "d":
		io.output(dL1, True)
		io.output(dL2, False)
		io.output(dR1, False)
		io.output(dR2, True)
		pL.start(100)
		pR.start(100)
	elif direction == "a":
		io.output(dL1, False)
		io.output(dL2, True)
		io.output(dR1, True)
		io.output(dR2, False)
		pL.start(100)
		pR.start(100)
	elif direction == "x":
		pL.stop()
		pR.stop()		
        else:
                pL.stop()
                pR.stop()
                #io.cleanup()
	
	#reply = 'OK...' + data + '\r\n'
	#if not data: 
	#	break
	
	#conn.sendall(reply)
io.cleanup()
conn.close()
s.close()
