class dad:



    def  __init__(self,eyes,aggressive):
        self.eyes=eyes
        self.aggressive= aggressive


    def display(self):
        print("your eye color is",self.eyes)
        print ("you are aggressive",self.aggressive)


class son (dad):
    def __init__(self,name,age,eyes,aggressive):
        self.name=name
        self.age = age



        dad.__init__(self,eyes,aggressive)
obj= son("paarth",12,"browen" , False)

































































































obj.display()