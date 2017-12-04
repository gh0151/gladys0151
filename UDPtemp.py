from socket import *
import time
from UDP_RGB import readRGB
address = ('192.168.1.100', 6454)

client_socket = socket(AF_INET, SOCK_DGRAM) #Set Up the Socket
client_socket.settimeout(2) #only wait 2 seconds for a response

temp=0
while True: #Main Loop
    data = "Blue" #Set data to Blue Command
    client_socket.sendto(data.encode(), address) #send command to MASTER

    try:
        print("BLUE WAS SENT\n")
        rec_data, addr = client_socket.recvfrom(2048) #Read response from MASTER
        print(rec_data.decode()) #Print the response from MASTER
        print(rec_data) #Print the response from MASTER

	if (rec_data.decode() == 'LUX'):
        	#luxValue = readRGB()
            luxValue = "RGB N/A at the momment."
            data = 'Current Lux Value is' + luxValue + ' : '
            client_socket.sendto(data.encode(), address) #send LUX to MASTER


    except:
        print("FIRST ERROR\n")
        pass
	print('You should not read this!!!!!!')


    if (temp < 10):
        print("Temp %d"%temp)
	temp = temp + 1

    if ((temp + 1) == 1):
	break


