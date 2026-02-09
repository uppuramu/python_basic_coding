# create 2 classes and use inheritance print the all information 
# of class 1 with class 2

class A1():
    print('class 1')
    def ab(self):
        print('class 1 metod..')

class A2(A1):
    print('class 2')
    def abc(self):
        print('class 2 metod..')

obj=A2()
obj.ab()
obj.abc()