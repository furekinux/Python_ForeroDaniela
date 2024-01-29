n=(int(input()))

def coins():
    a=[(int(n/10)),(int((n%10)/5)),(int(((n%10)%5)/1))]
    print(a)

coins()