# Import socket module 
import socket			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 23				

# connect to the server on local computer 
s.connect(('94.142.241.111', port)) 
breakpoint()
# receive data from the server 
total_data = []
data='';
while True:
    data = s.recv(8196)
    if data:
        print(data)
        total_data.append(data)
    else:
        break
#Process data
rcv_data = "\n".join(rcv_data.split('\n'))

print(rcv_data)
# close the connection 
s.close()	 

