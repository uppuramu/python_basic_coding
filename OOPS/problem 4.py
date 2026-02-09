# create a class with name marks ans create a method to get marks 
# create anoter method to finsd avarage

class Marks():
    total=0
    n=0
    def stmarks(self):
        self.n=int(input('enter no subjects:'))
        for i in range(0,self.n):
            self.m=int(input('enter marks:'))
            self.total=self.total+self.m
            print(self.total)
    def avg(self):
        a=self.total/self.n
        print(a)

obj=Marks()
obj.stmarks()
obj.avg()
