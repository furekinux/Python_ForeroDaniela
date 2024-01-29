n=(int(input()))

def coins():
    global a
    a=[f"Monedas $10: {(int(n/10))}",f"Monedas $5: {(int((n%10)/5))}",f"Monedas $1: {(int(((n%10)%5)/1))}"]
    print(a)
coins()