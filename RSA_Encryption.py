#RSA Algorithm
#Done! Step 1: Take two large distinct primes p and q
#Step 2: Multiply p and q and store in n
#Step 3: Find the toitent for n (phi = p-1*q-1)
#Step 4: Find e which is coprime between 1 and n
#Step 5: find d using d*e = 1 mod phi(n)
#note: (e,n) is public key, (d,n) is private key
#Step 6: Encrypt the message and Decrypt the ciphertext

import random
import math

def modularExpo(x,p):
    #a==base b == exponent c == mod
    binaryNumber = [int(i) for i in list('{0:0b}'.format(p-1))]
    binaryNumber.reverse()
    powersOfTwo = list()
    for i in range(len(binaryNumber)):
        if i == 0 or i == 1:
            powersOfTwo.append(2**i)
        else: 
            powersOfTwo.append((powersOfTwo[i-1]**2)%p)
    x = 1
    for i in range(0, len(binaryNumber)):
        if binaryNumber[i] == 1:
            x = (x* powersOfTwo[i]) % p
    return x


def binaryExpo(a,b):
    res = 1
    while b>0:
        if b&1:
            res = res*a
        a = a*a
        b >>=1
    return res

def binpow(a,b,m):
    a %=m
    res = 1
    while b>0:
        if b&1:
            res = res*a%m
        a = a*a%m
        b >>=1
    return res

def isPrime(n):
    prime = False
    if ((modularExpo(2,n) == 1)):
        prime = True
    return prime
    

def generateLargePrime(k):
    while True:
        n = random.randrange(2**(k-1), (2**k))
        if (isPrime(n) == True): 
            break
    return n

def euclid(a,b):
    if a == 0:
        return b

    return euclid(b%a,a)

def euclidExtended(a,b):
	if a == 0:
    		return (b, 0, 1)
	else:
		gcd, x, y = euclidExtended(b % a, a)
		return (gcd, y - (b//a) * x, x)

def encrypt(key, message):
    print("In the function")
    e, n = key
    send = binpow(message, e,n)
    print("about the leave the function")
    return send

def decrypt(publicKey, privateKey, cipher):
    d, n = privateKey
    send = binpow(cipher, d, n)
    return send
def modInverse(a, m):
    m0 = m 
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (a > 1) : 
        # q is quotient 
        q = a // m 
        t = m 

        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 
def main():
    print("Welcome to my RSA program!")
    print("Step 1: Generate p and q:")
    #p = large prime 
    print("Generating P...")
    p = generateLargePrime(k=1000)
    #q = Large prime
    print("Generating Q...")
    q = generateLargePrime(k=1000)
    while abs(p-q) < 10**95:
         q = generateLargePrime(k=1000)
   
    print("Step 1 Completed.\n Step 2: Generate N.")
    n = p*q
    print("Step 2 Completed. \n Step 3:Find the toitent for n (phi = p-1*q-1) ")
    phi = (p-1) * (q-1)
    print("Step 3 Completed. \n Step 4: Find e which is coprime between 1 and n ")
    e = 65537
    while euclid(e, phi) != 1:
        e = random.randrange(1,phi)
    print("Step 4 Completed. \n Step 5: Find d using d*e = 1 mod phi(n) ")
   # gcd, x,y  = euclidExtended(e, phi)
    d = modInverse(e,phi)
    print("Step 5 Completed.\n Private and public keys have been generated.")
    #private key = d,n // public key = e,n
    publicKey = e, n
    privateKey = d, n 
    f = open("message.txt", "r+") #open file containing plaintext
    plaintext = int(f.read()) #read the plntext into variable pText
    pPrivate = open("private_key.txt", "a+")
    pPrivate.write("\nPrivate Key:\n")
    pPrivate.write("D: ")
    pPrivate.write(str(d))
    pPrivate.write("\nN: ")
    pPrivate.write(str(n))
    pPublic = open("public_key.txt", "a+")

    pPublic.write("\nPublic Key:\n")
    pPublic.write("E: ")
    pPublic.write(str(e))
    pPublic.write("\nN: ")
    pPublic.write(str(n))
    pPrivate.close()
    pPublic.close()

    print("Private and Public keys saved\n Step 6: Encryption and Decryption ")
    print("Encrypting...")
    ciphertext = encrypt(publicKey, plaintext)
    print("returned from function")
    print(ciphertext)
    pCipher = open("ciphertext.txt", "a+")
    pCipher.write("\n")
    pCipher.write(str(ciphertext))
    pCipher.close()
    print("The message has been converted to ciphertext.")
    print("Decrypting...")
    decryptedText = decrypt(publicKey, privateKey, ciphertext)
    pDecrypt = open("decrypted_message.txt", "w+")
    pDecrypt.write("\n")
    pDecrypt.write(str(decryptedText))
    pDecrypt.close()

    print("Your decrypted message is %s" %decryptedText)
    print("The original message was %s" %plaintext)
    if decryptedText == plaintext:
        print("SUCCESS!!")
main();
   