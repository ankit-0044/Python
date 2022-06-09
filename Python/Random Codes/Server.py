import socket
def sharedkey(x):
    A=str(int(pow(10,x,19)))
    return A
s=socket.socket()
print("Socket created...")
s.bind(('localhost',9999))
s.listen(3)
print("waiting for connection..")
while True:
    c,addr=s.accept()
    message=c.recv(1024).decode()

    print("Connected with",addr,message)
    x=int(input("Enter your private key: "))

    c.send(bytes("This is your client...",'utf-8'))
    c.send(bytes(sharedkey(x),"utf-8"))
    B = int(c.recv(1024).decode())
    print("B = ",B)
    ka = int(pow(B,x,19))
    print("Secret key generated = ",ka)

    c.close()
