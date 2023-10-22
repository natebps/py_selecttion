m,y = [int(e) for e in \
    input("Month and Year: ").split()]
y1 = y - 543


if m in (1,3,5,7,8,10,12):
    print("31")
elif m in (4,6,9,11):
    print("30")
elif m == 2 and \
    y1%4 == 0 and y1%100 != 0:
    print("29")
elif m == 2 :
    print("28")