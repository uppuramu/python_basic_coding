# find area pf cicle using inheritence concept

class Area():
    ar=0
    def ab(self):
        print('area of circle..')
        r=int(input('enter radius:'))
        self.ar=1.314*r*r

class Show(Area):
    def abc(self):
        print(self.ar)
        
obj=Show()
obj.ab()
obj.abc()
