#This is the Receiver/ Gateway/ Server Node
#This node receives data from multiple sender nodes
import socket, time
import datetime

UDP_IP = '192.168.1.6'
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

file = open('received_data','w')


while True:
    msg, addr = sock.recvfrom(1024)
    now = datetime.datetime.now()
    #print('time:', time.now())
    print('Time:', now,'RECV', msg.decode())
    rcvd_msg = f'Time: {now} RECV {msg.decode()}'
    file.write(rcvd_msg +'\n')


file.close()