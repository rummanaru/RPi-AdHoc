#Sends sensor data to a target Receiver/ Gateway
import socket, time, sys
import datetime

Rcvr_UDP_IP = '192.168.1.6'
Rcvr_UDP_Port = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

file = open('sent_data.txt','w')

i = 1
while True:
    now = datetime.datetime.now()
    print('MSG Sent. Time:',now)
    MESSAGE = f'Hello World {i}: , Node1_Send_time:{now}'
    
    sock.sendto(MESSAGE.encode(), (Rcvr_UDP_IP, Rcvr_UDP_Port))
    file.write(MESSAGE +'\n')
    
    #time.sleep(1)
    time.sleep(float(sys.argv[1]))
    i += 1
    
file.close()
