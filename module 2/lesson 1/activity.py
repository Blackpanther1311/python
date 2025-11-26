medical_cause = input("do you have a medical cause?(Y OR N):")
attendance =int(input ("enter your attendance: "))
if medical_cause == "N":
    if attendance < 75:
        print("you are not allowed to sit in then exam.")
    else:
        print("you allowed to sit in the exam.") 
else:
    print("you are allowed to sit on exam.")        