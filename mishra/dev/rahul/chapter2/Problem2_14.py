'''
Created on 04-Sep-2016
@author: Rahul Dev Mishra
'''

def fibonacci(fibTerm):
    firstTerm = 1
    secondTerm = 1
    nextFibNum = firstTerm + secondTerm
    numberOfTerms = 3
    print(firstTerm, secondTerm, nextFibNum, end =" ")
    while(numberOfTerms <= fibTerm):
        secondTerm = firstTerm
        firstTerm = nextFibNum
        nextFibNum = firstTerm + secondTerm
        numberOfTerms = numberOfTerms + 1
        print(nextFibNum, end =" ")

print(fibonacci(5))        