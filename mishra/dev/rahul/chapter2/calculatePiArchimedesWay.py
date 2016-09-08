'''
Created on 25-Aug-2016

@author: aleesha
'''
import math
def calculatePiArchimedesWay(sides):
    innerAngle = 360 / sides
    halfInnerAngle = innerAngle / 2
    halfSide = math.sin(math.radians(halfInnerAngle))
    fullSide = halfSide * 2
    circumference = fullSide * sides
    return circumference / 2

piValue = calculatePiArchimedesWay(8)
print(piValue)
for sides in range(1, 100):
    print(sides, ":", calculatePiArchimedesWay(sides))