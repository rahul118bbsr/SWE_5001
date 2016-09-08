'''
Created on 04-Sep-2016
@author: Rahul Dev Mishra
'''
def calculatePi(terms):
    piValue = 0
    numerator = 4
    denominator = 1
    for term in range(terms):
        fraction = (numerator / denominator) * (-1) ** term
        piValue = piValue + fraction
        denominator = denominator + 2
    return piValue

terms = int(input("Enter the number of terms: "))
print(calculatePi(terms))
