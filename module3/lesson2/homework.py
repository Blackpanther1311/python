import os 

shutdown=input("do you want to shut dowen youre computer?(yes  /  no):")
if shutdown=='no':
    exit()
else:
    os.system("shutdown /s /t 1")