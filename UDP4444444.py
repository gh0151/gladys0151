#Client UDP
import socket
import sys
import time
                                    #Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#server_address is a 'Tuple' of 2 with values 'localhost' and 10000
server_address = ('192.168.1.101', 6454)

print("starting up on %s port %s \n" %server_address)

message = 'Hey server, What\'s up?'

temp1 = ''
while (temp1 != 'Bye, Client'):    
    

    sock.sendto(message.encode(), server_address)
    time.sleep(1)

    data, address = sock.recvfrom(4096)
    temp1 = data.decode()
    print(data.decode())

    time.sleep(2)
    sock.sendto('Adios, Server'.encode(), server_address)
    
    
print('Closing socket')
time.sleep(1)
sock.close()
