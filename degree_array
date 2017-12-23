#Using pandas is not cheating right

import pandas as pd
dirt = r'C:\Python\Rosalind\Degree_Array\rosalind_deg.txt'

foo = open(dirt, 'r')
data = foo.readlines()


num_list = []
#Skip first line of data
iter_data = iter(data)
next(iter_data)

#Adds every number to a list
for item in iter_data:
    num = item.split()
    num_list.append(num[0])
    num_list.append(num[1])
   
num_list = list(map(int, num_list))

s = pd.Series(num_list) 
listo = s.value_counts()
listo.sort_index(inplace=True)
print(*list(listo))
