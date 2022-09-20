import turtle
bob = turtle.Turtle()
print(bob)
def square(t,length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)
square(bob,200)
def polygon(t,length,n):
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)
polygon(bob,100,6)
def circle(t,length,n):
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)
circle(bob,3,30)
def arc(t,length,n,angle):
    for i in range(n):
        bob.fd(length)
        bob.lt(angle/n)
arc(bob,6,40,360)
turtle.mainloop()