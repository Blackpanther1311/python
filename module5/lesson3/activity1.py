class student:
    __schoolname="xyz school"

    def __init__(self,name,age):
        self.__name= name



    def __display(self):
        print("thisis a private method")


std=student("bill",15)
print(std.__schoolname)