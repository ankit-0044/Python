#Attacker program acting as client for victim's server
import socket
def sharedkey(y):
    B = str(int(pow(10,y,19)))
    return B

c = socket.socket()
c.connect(('localhost',9999))
message = input('Enter your message : ')
y = int(input("Enter your virtual private key for client pairing with actual server : "))
c.send(bytes(message,'utf-8'))
c.send(bytes(sharedkey(y),'utf-8'))
print(c.recv(1024).decode())
A = int(c.recv(1024).decode())
print("A = ",A)
kb = int(pow(A,y,19))
print("Secret key generated for server and man_ in_the_middle communication = ",kb)

#Attacker program acting as server for victim's client
def Sharedkey(x):
    A = str(int(pow(10,x,19)))
    return A
s = socket.socket()
s.bind(('localhost',9990))
print("socket created ...")
s.listen(3)
print('Waiting for connection.......')

while True:
    c, addr = s.accept()
    message = c.recv(1024).decode()
    print('Connected with ',addr,message)
    x = int(input("Enter your virtual private key for server pairing with actual client : "))

    c.send(bytes('Welcome to the server |||||||||||......','utf-8'))
    c.send(bytes(Sharedkey(x),'utf-8'))
    B = int(c.recv(1024).decode())
    print("B = ",B)
    ka = int(pow(B,x,19))
    print("Secret key generated for man_in_the_middle and client communication = ",ka)
    c.close()
