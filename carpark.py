h1 = int(input("Hours in: "))
m1 = int(input("Minutes in: "))
h2 = int(input("Hours out: "))
m2 = int(input("Minutes out: "))
#time open-close
if h1 < 7:
    print("NOT OPEN KA")
elif h2 > 23:
    print("CLOSE LAEW KA")
#calculate money
timein = (h1*60)+m1
timeout =(h2*60)+m2
timetotal = timeout-timein

if timetotal <= 15:
    print("0")
elif 15<= timetotal <60:
    print("10")
elif 60 <= timetotal <=180:
    print((h2-h1)*10)
elif 180< timetotal <=360:
    print((h2-h1)*20)
elif 360< timetotal:
    print("200")
