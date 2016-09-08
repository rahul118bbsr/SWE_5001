'''
Created on 06-Sep-2016
@author: Rahul Dev Mishra
'''

def encrypt(word):
    oddChars = ""
    evenChars = ""
    charCount = 0
    for ch in word:
        if(charCount % 2 == 0):
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount += 1    
    cipher = oddChars + evenChars
    return cipher

word = input("Enter the word to encrypt:")
print("Encrypted Word:",encrypt(word))        