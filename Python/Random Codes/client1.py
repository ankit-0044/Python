import socket             
  
s = socket.socket()         
  
port = 8080           
  
s.connect(('127.0.0.1', port)) 
  
# receive data from the server 
data = s.recv(1024)
print("Key received from server is:",data) 
