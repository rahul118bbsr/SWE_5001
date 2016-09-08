'''
Created on 06-Sep-2016
@author: Rahul Dev Mishra
'''
import random
def encrypt(plainText, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    plainText = plainText.lower()
    cipher = ""
    for char in plainText:
        index = alphabets.index(char)
        cipher = cipher + key[index]
    
    return cipher

def keyGen():
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    key = ""
    for i in range(26):
        char = alphabets[random.randint(0, 25 - i)]
        key = key + char
        alphabets = removeChar(alphabets, char)
    
    return key   

def removeChar(word, charToRemove):
    index = word.index(charToRemove)
    if(index < 0):
        print("Cannot remove the letter:", charToRemove, "from the word:", word) 
    
    word = word[:index] + word[index + 1:]  
    return word

plainText = input("Enter a word to encrypt:")
key = keyGen()
print("Key:", key)
print("Decrypted Word:", encrypt(plainText, key))