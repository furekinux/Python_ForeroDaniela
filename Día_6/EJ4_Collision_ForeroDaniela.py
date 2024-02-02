def ballcollide():
    if m<=rad_sum:
        return True
    else:
        return False

DiccioA={}
DiccioB={}
a_Cor=[]
b_Cor=[]
##Diccio A
u=DiccioA
print("\nType the coordinates then the radius of the ball A.")
Coordinates_a=input("").split(" ")
u=Coordinates_a
x=int(u[0])
y=int(u[1])
r=int(u[2])
a_Cor=(x,y,r)
CorListA=[a_Cor]
radiusA=r

#Diccio B
v=DiccioB
print("\nType the coordinates x and y then the radius of the ball A.")
Coordinates_b=input("").split(" ")
v=Coordinates_b
x=int(v[0])
y=int(v[1])
r=int(v[2])
b_Cor=(x,y,r)
CorListB=[b_Cor]
radiusB=r

rad_sum=radiusA+radiusB

print("\nThe ball A's coordinates and radius are: ",a_Cor)
print("The ball B's coordinates and radius are: ",b_Cor)

m=int(input("\nHow long is the distance between them: "))
print("\nColliding?")
print(ballcollide())
##Hecho por Daniela Forero 1142714227 ;-;