'''
Created on 06-Sep-2016
@author: Rahul Dev Mishra
'''

def decrypt(cipher):
    halfLength = len(cipher) // 2
    oddChars = cipher[:halfLength]
    evenChars = cipher[halfLength:]
    word = ""
    for i in range(halfLength):
        word = word + evenChars[i]
        word = word + oddChars[i]
    
    if(len(evenChars) > len(oddChars)):
        word = word + evenChars[-1]

    return word    
cipher = input("Enter the word to decrypt:")
print(decrypt(cipher))