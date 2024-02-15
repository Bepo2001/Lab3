Flag="yes"
data={}
while Flag!="no":


    name=input("please enter name of the employee: ")
    salary=input("please enter salary of the employee: ")

    data[name]=salary

    Flag=input("if you want to stop type 'no' or else type anything ")
print(data)


