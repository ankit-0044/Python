#encryption

def encrypt(string, key):
 
  cipher = ''
  
  for char in string: 
    if char == ' ':
      cipher = cipher + char
      
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + key - 65) % 26 + 65)

    else:
      cipher = cipher + chr((ord(char) + key - 97) % 26 + 97)
  
  return cipher
 
text = input("Enter string: ")
s = int(input("Enter key number: "))
print("Original string: ",text)
print("After encryption: ",encrypt(text, s),'\n\n')

#Decryption

def decrypt(string, key):
 
  cipher = ''
  
  for char in string: 
    if char == ' ':
      cipher = cipher + char
      
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - key - 65) % 26 + 65)

    else:
      cipher = cipher + chr((ord(char) - key - 97) % 26 + 97)
  
  return cipher
 
text = input("Enter cipher text: ")
s = int(input("Enter key number: "))
print("Cipher string: ",text)
print("After decryption: ",decrypt(text, s))

