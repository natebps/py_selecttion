x1,y1,r1 = [float(e) for e in \
     input("X: ").split()]
x2,y2,r2 = [float(q) for q in \
     input("X: ").split()]
d = (x1-x2)**2 + (y1-y2)**2
sumr2 = (r1+r2)**2

if d < sumr2:
    print("overflow")
elif d == sumr2:
    print("touch")
else:
    print("free")