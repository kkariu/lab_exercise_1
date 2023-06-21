def calculator(a,b,c,ops1,ops2):
    if ops1 == "+":
        result=a+b 
    elif ops1=="-":
        result =a-b
    elif ops1=="*":
        result=a*b
    elif ops1=="/":
        result=a/b 
    else:
        print("enter correct operation")
        return None
    
    if ops2 == "+":
        result+=c
    elif ops2=="-":
        result-=c
    elif ops2=="*":
        result*=c
    elif ops2=="/":
        result/=c
    else:
        print("enter correct operation")
        return None
    
    return result
firstnumber =float(input("enter the first number"))
firstoperation=input("enter first operaion(+-*/)")
secondnumber=float(input("enter the second number"))
Secondoperation=input("entre the second operation(+-*/)")
thirdnumber=float(input("entre the third number"))

answer=calculator(firstnumber,secondnumber,thirdnumber,firstoperation,Secondoperation)

if answer is not None:
    print("result:",answer)

