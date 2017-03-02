import socket

def forward():
        print ('go forward')

def reverse():
        print ('reverse')

def right():
        print ('turn right')

def left():
        print ('turn left')

def stop():
        print ('stop')


clisock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
clisock.connect( ('192.168.15.35', 23000) )
while 1:
        message = (clisock.recv(10))
        if message == "8":
                forward()
        if message == "2":
                reverse()
        if message == "6":
                right()
        if message == "4":
                left()
        if message == "5":
                stop()

clisock.close()
