'''
Created on 04-Sep-2016

@author: Rahul Dev Mishra
'''

def factorial(num):
    factorial = 1
    while(num > 0):
        factorial = factorial * num
        num = num - 1
    return factorial

print("Factorial of 4:", factorial(4))