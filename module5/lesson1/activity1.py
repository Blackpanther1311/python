class vegetable:
    #constructor
    def __init__(self,name, color):
        self.name=name 
        self.color=color

#object creation
obj=vegetable('carrot','light red')

print("the name of the  vegtable is",obj.name,".the coior is",obj.color)
