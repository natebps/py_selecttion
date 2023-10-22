g = float(input("Input Grade: "))

if 80 <= g <= 100:
    print("A")
elif 75 <= g < 80:
    print('B+')
elif 70 <= g < 75:
    print('B')
elif 65 <= g < 70:
    print('C+')
elif 60 <= g < 65:
    print('C')
elif 55 <= g < 60:
    print('D+')
elif 50 <= g < 55:
    print('D')
elif 0 <= g < 50:
    print("F")
else:
    print("error")