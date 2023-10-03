a= int(input("enter the value"))
opp= input("enter the function + ,- ,*,/")
b= int(input("enter the value")) 
   
if opp == '+':
        print(a,opp,b,"=",a+b)
elif opp == '-':
        print(a,opp,b,"=",a-b)
elif opp == '*':
        print(a,opp,b,"=",a*b)
elif opp == '/':
        print(a,opp,b,"=",a/b)
else:
        print ("syntax error")
