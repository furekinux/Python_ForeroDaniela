##AAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHH
n=(int(input()))
def coins():
    if n>=1 and n<=1000:
        print(f"{(int(n/10))+(int((n%10)/5))+(int(((n%10)%5)/1))}")
    else: 
        print("ERROR")
coins()
##Realizado por Daniela Forero :D 1142714225