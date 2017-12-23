
dirt = r'C:\Python\Rosalind\rosalind_ins.txt'
reado = open(dirt, 'r')
data = reado.readlines()

for item in data:
    foo = item.split()
foo = list(map(int, num))

bar = range(len(foo))

bar_iter = iter(bar)
next(bar_iter)

counter = 0
for i in bar_iter:
    k = i
    
    while k > 0 and (foo[k] < foo[k-1]):
        temp = foo[k]
        foo[k] = foo[k-1]
        foo[k-1] = temp
        counter += 1
        k = k-1
print(str(counter) + ' attempts')
