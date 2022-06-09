import socket
def sharedkey(y):
    B=str(int(pow(10,y,19)))
    return B
b=socket.socket()
b.connect(("localhost",9990))
message=input("Enter your message : ")
y=int(input("Enter your private key: "))
b.send(bytes(message,"utf-8"))
b.send(bytes(sharedkey(y),"utf-8"))
print(b.recv(1024).decode())
A = int(c.recv(1024).decode())
print("A = ",A)
kb = int(pow(A,y,19))
print("Secret key generated = ",kb)
b.close()
