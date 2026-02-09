# get integer input from one method1 and print same input in  method 2 using class

class Ab():
    n=0
    def a(self):
        self.n=int(input('enter numbe:'))
    def b(self):
        print(self.n)

obj=Ab()
obj.a()
obj.b()