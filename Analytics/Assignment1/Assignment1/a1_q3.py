# Python program to compute the (GCD) of the squares of two positive integers.
from math import gcd

print('Running A1_Q3')
a, b = [int(x) for x in input('Enter 2 positive integers: ').split()]
if(a <= 0 or b <= 0):
    print('Invalid input! Enter only positive integers')
    exit()
print("GCD of their squares: {gcds}".format(gcds = gcd(a ** 2, b ** 2)))
