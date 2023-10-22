x,y = [float(e) for e in \
     input("No.: ").split()]

if x == 0 and y == 0:
    print('At the origin')
elif x == 0:
    print("On y-axis")
elif y== 0:
    print('On x-axis')
elif x and y > 0:
    print('Q1')
elif x < 0 and y > 0 :
    print('Q2')
elif x and y < 0:
    print('Q3')
else:
    print('Q4')