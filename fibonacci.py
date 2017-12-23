def fib(num):
    if num==0:
        return 0
    if num==1:
        return 1
    
    foo = []
    foo.append(0)
    foo.append(1)

    n=2
    last_n=0
    while n <= num:
        last_n = foo[-1] + foo[-2]
        foo.append(last_n)
#         print(foo)
        n+=1
    
    return foo[-1]
    
    
