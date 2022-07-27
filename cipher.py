#Darryl Alexander Fleurantin
#04/04/2022
#CSC 110 Homework 7 Cryptography

import random

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

#random caeser shift function
def caesarRandom(plaintext, seedIn):
    random.seed(seedIn)
    ciphertext = ""
    plaintext = plaintext.lower()
    plaintext = plaintext.replace(" ","")
    for i in range(len(plaintext)):
        num = random.randint(0, 25)
        letter = plaintext[i]
        num_in_alphabet = alphabet.index(letter) 
        cipher_num = (num_in_alphabet + num) % len(alphabet) 
        cipher_letter = alphabet[cipher_num] 
        ciphertext = ciphertext + cipher_letter 
    return ciphertext
#function to unshift random
def unCaesarRandom(ciphertext, seedIn):
    random.seed(seedIn)
    deCiphertext = ""
    for i in range(len(ciphertext)):
        num = random.randint(0, 25)
        letter = ciphertext[i] 
        num_in_alphabet = alphabet.index(letter) 
        cipher_num = (num_in_alphabet - num) % len(alphabet) 
        cipher_letter = alphabet[cipher_num] 
        deCiphertext = deCiphertext + cipher_letter 
    return deCiphertext

#Analysis:
#This algorithm is better than the caesar cipher because it's more complex and more unpredictable.
#It can be broken down once the seed is found or with cross-referencing.
