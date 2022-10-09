# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:22:13 2022

@author: Fawzia Al-Bluwi - CS 538 Applied Cryptography
"""

import secrets
import string

# A key generation algorithm using Secrets module that uses cryptographically secure random function to generate key
def genKey(length):

    key = ''
    for i in range(length):
        key += ''.join(secrets.choice(string.ascii_uppercase + string.digits))

    return key

# One-time pad encryption function - encrypts message m using key k to produse ciphertext c
def OTP_encrypt(m, k):
    
    # Check the length of both m and k (should be similar)
    if len(m) != len(k):
        print ('The message and the key lengths are not the same.')
        exit()
        
    
    # Encrypt the message using One-Time Pad (XOR Operation)
    c = ''
    for a,b in zip(m, k):
        c += chr(ord(a) ^ ord(b)) #The ord() method has been applied to each byte of a string of both variables separately to take one byte each time
    
    return c

# One-time pad decryption function - gets message m through decrypt ciphertext c and key k
def OTP_decrypt(c,k):
        
    # Check the length of both c and k (should be similar)
    if len(c) != len(k):
        print ('The ciphertext and the key lengths are not the same.')
        exit()
    
    # Decrypt the ciphertext using One-Time Pad (XOR Operation)
    m = ''
    for a,b in zip(c, k):
        m += chr(ord(a) ^ ord(b)) #The ord() method has been applied to each byte of a string of both variables separately to take one byte each time
    
    return m

#/////////////////////////////////////////////////////////////////////////////

choice = int(input("Welcome to One-Time Pad Encryption\n Choose your mode of input\n 1. Type the text in the prompt.\n 2. Type the file path of the text.\n"))

if(choice == 1):
    dataToEncrypt = input("Enter your data:\n")
elif(choice == 2):
    pathToDataFile = input("Enter full file path:\n")
    file = open(pathToDataFile, 'rt')
    dataToEncrypt = file.read()
    file.close()
else:
    print("Wrong choice. Bye!")
    exit()

# Show the data    
print("Data to encrypt is \n\"\n", dataToEncrypt, "\n\n\"\n")

# Get the length of the data
dataLength = len(dataToEncrypt) 
print("The length of data is ", dataLength)

# Generate cryptic key of the same length of data
print("... generating key")
keyToUse = genKey(dataLength)

# Show the generated key
print("The generated key is \n\"\n", keyToUse, "\n\n\"\n")

# Encrypt the data using the key
encryptedData = OTP_encrypt(dataToEncrypt, keyToUse)

# Show the encrypted data
print("The encrypted data is \n\"\n", encryptedData, "\n\n\"\n")

# Store the encrypted data into a file
outFile = open(r'C:\Users\USER\Desktop\2022 Desktop\ciphertext.txt', 'w')
outFile.write(str(encryptedData.encode("utf-8")))
outFile.close()

# Decode the data using the key
decryptedData = OTP_decrypt(encryptedData, keyToUse)

# Show the decrypted data
print("The decrypted/original data is \n\"\n", decryptedData, "\n\n\"\n")

# Close the program
print("The encrypted data stored into ciphertext.txt.\nThe end of program. Bye!")
