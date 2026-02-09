# by using class take a number and print it's table

class table():
    num=0
    def get(self):
        self.num=int(input('enter number:'))
    
    def show(self):
        for i in range(1,11):
            print(self.num,'*',i,'=',i*self.num)
        
obj=table()
obj.get()
obj.show()    
        
        