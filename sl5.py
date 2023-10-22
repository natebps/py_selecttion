a,b,c,d = [int(e) for e in \
        input('Numbers: ').split()]
mx = a
if b > mx: mx =b
if c > mx: mx =c
if d > mx: mx =d
mn = a
if b< mn: mn = b
if c< mn: mn = c
if d< mn: mn = d
total = (a+b+c+d)-mx-mn
print(total)