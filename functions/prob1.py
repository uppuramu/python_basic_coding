# find area of circle and square

from re import A


def area(r,s):
    carea=3.14*r*r
    print('area of circle:',carea)
    sarea=s*s
    print('area of sqare:',sarea)

radius=float(input('enter radius:'))
side=int(input('enter lenth:'))
area(radius,side)