# Python program to calculate its future value, after a given number of years and compounding rate of growth.

def compound_interest(principle, rate, time):
 
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    return CI

print("Running a1_q4")
principle = int(input("Enter the principle amount:"))
rate = float(input("Enter the rate of interest:"))
period = float(input("Enter the period:"))

print("The calculated future value: {}".format(compound_interest(principle, rate, period)))
