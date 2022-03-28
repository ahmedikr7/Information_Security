#Ahmed Ikram, 22-10019, InfoSecurity Assignment #2. Due: 26/01/22
import cryptography
import rsa 

print("|-----Welcome to Ahmed Ikram's assignment-2, INFOSECURITY Section:A-----|\n")

key_public, key_private= rsa.newkeys(1024)# I have set the length of the string to a long length.

print("USER PUBLIC KEY:\n",key_public,"\n")
print("USER PRIVATE KEY:\n",key_private,"\n")
msg = input("[Enter plain text to encrypt:]\n\n") #The original plain text in the msg variable.

msg_encrypted = rsa.encrypt(msg.encode(),key_public)
#Builtin rsa.encrypt, encrypts variable msg turning into string type byteString.
 
print("\n[Non-encrypted Plain text string:]\n\n", msg)
print("\n[Encrypted plain text string:]\n\n", msg_encrypted)
 
msg_decrypted = rsa.decrypt(msg_encrypted, key_private).decode()
#Builtin method of rsa.decrypt shall decrypt the data in msg_encrypted variable.
#The byetString is reconverted into string format.
print("\n[Decrypted string:]\n\n", msg_decrypted)
