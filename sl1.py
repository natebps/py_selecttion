a,b,c = [int(e) for e in \
    input("Input: ").split()]
if c <= a <= b or b <= a <= c:
    print(a)
elif a<= b<= c or c<= b<= a:
    print(b)
else:
    print(c)
