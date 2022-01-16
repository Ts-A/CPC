from math import nan
import pandas as pd
  
dict = {'Person_A':['First_Name_A', nan, 95],
        'Person_B': ['First_Name_B', 56, nan],
        'Person_C':['First_Name_C', 80, 98]}
  
df = pd.DataFrame(dict)

print("Running a1_q7.py")
print("Values which are left empty/ null will return false.")  
print(df.notnull())