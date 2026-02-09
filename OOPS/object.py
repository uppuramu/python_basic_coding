# object is created from class name
# object contain attributes and behaviour
# after creating  class ,itneeds to create a object
# using object developer can access attributes,methoda from class
# any class contain more than one object

#  ex:  car,dog,pen,etc

# syntax:  class classname:
                 #code
            
           #objectname=classname()  
 
 # creation of class          
class Abc:
    a=10
    b=20
    print('qwerty')
    def show(self):
        print('hi')
        print(self.a)
        print(self.b)
        
# creation object     
obj=Abc()
#obj.show()
print(obj.a)
print(obj.b)

        
        