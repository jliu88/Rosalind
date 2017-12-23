from math import log, ceil

dirt = r'C:\Python\Rosalind\Binary_Search\rosalind_bins.txt'

foo = open(dirt)
data = foo.readlines()

num_list = []
for item in data:
    num = item.split()
    num_list.append(num)
    
s_array = list(map(int, num_list[2]))
m_list = list(map(int, num_list[3]))    

ans_list = []
max_attempt = ceil(log(len(s_array),2))

for targ in m_list:
    lower = 0
    upper = len(s_array) - 1
    loc = 0    
    counter = 1

    while s_array[loc] != targ and loc != -2:
        loc = (lower + upper)//2
        num = s_array[loc]

#         print(str(counter) + ')' + 'loc: ' + str(loc) + ' val: ' + str(num))

        if counter < max_attempt + 1:
            if num < targ:
                lower = loc
            if num > targ:
                upper = loc
            counter += 1

        else:
            loc = -2

#     print(str(targ) + ' found at location:' + str(loc) + ' with ' + str(counter-1) + ' attempts')
    ans_list.append(loc+1)
    
    
    
print(*ans_list)
