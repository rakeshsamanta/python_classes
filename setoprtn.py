#Define set of operation
from typing import Union


E = {0,2,4,6,8}
N = {1,2,3,4,5}

#UNION OF NUMBER
print("Union of E & N" , E | N)

#SET DIFFERENCE
print("Difference of E & N", E - N)

#SET INTERSECTION
print("Intersection of E & N",E & N)

#SET SYMMETRIC DIFFERENCE
print("Symmetric difference of E and N",E ^ N)
