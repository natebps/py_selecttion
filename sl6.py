a = int(input("A: "))
x = int(round(a**(1/3),0))
if x**3 != a:
    print("NOT FOUND")
else:
    print(x)
