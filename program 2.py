PI = 3.14
def areaOfCircle(radius):
    area = PI*radius*radius
    return area

def circOfCircle(radius):
    circ = 2*PI*radius
    return circ

radius = input()
radius = float(radius)

area = areaOfCircle(radius)
print('area of circle is:%d'%area)

circ = circOfCircle(radius)
print('circumference of circle is:%d'%circ)
