import turtle
bob = turtle.Turtle()
print(bob)
#desenha um quadrado com medida do lado definida por length
def square(t,length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)
square(bob,200)
#desenha um poligono de n lados com medida do lado definida por length
def polygon(t,length,n):
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)
polygon(bob,100,6)
#desenha um circulo aproximado 
def circle(t,length,n):
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)
circle(bob,3,30)
#desenha partes de um circulo aproximado, definido por angle
def arc(t,length,n,angle):
    for i in range(n):
        bob.fd(length)
        bob.lt(angle/n)
arc(bob,6,40,360)
turtle.mainloop()
