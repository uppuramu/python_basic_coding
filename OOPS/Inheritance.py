# it is process to create class from main class.the result class = derived class
# using inheritance we can access all method and attributes of main class in derived class

class Abc1():    # parent class
    print('1')
    def a(self):
        print('2')
        
class Abc2(Abc1):    # child class/derived class 
    print('3')
    def b(self):
        print('4')
obj=Abc2()
obj.a()
obj.b()
qw=Abc1()
qw.a()
#qw.b()  --show error

        