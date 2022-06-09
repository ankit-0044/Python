from random import randint
 
if __name__ == '__main__':
 
  
    Pub_key1 = int(input("Enter public key for Sagar: "))
    Pub_key2 = int(input("Enter public key for Rajan: "))
    print()

    print(f"The Value of public key for Sagar is: {Pub_key1}")
    print(f"The Value of public key for Rajan is: {Pub_key2}")
    print()

    Private_key1 = int(input("Enter private key for Sagar: "))
    print(f"The Private Key for Sagar is: {Private_key1}")
    x = int(pow(Pub_key2,Private_key1,Pub_key1)) 
    print()

    Private_key2 = int(input("Enter private key for Rajan: "))
    print(f"The Private Key for Rajan is: {Private_key2}")
    y = int(pow(Pub_key2,Private_key2,Pub_key1)) 
    print()
     
    Secret_key1 = int(pow(y,Private_key1,Pub_key1))
    Secret_key2 = int(pow(x,Private_key2,Pub_key1))
     
    print(f"Secret key for the Sagar is: {Secret_key1}")
    print(f"Secret Key for the Rajan is: {Secret_key2}")
