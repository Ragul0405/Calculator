class parent():
    def add(self, a,b):
        c=a+b
        print(a,"+",b,"=",c)
class child(parent):
    def sub(self,a,b):
        c=a-b
        print(a,"-",b,"=",c)
class child1(child):
    def mul(self,a,b):
        c=a*b
        print(a,"*",b,"=",c)
class child2(child1):
    def div(self,a,b):
        c=a/b
        print(a,"/",b,"=",c)

a=int(input("Enter Your A Value : "))
b=int(input("Enter Your B Value : "))
print("for ADD Use +")
print("for SUB Use -")
print("for MULTI Use *")
print("for DIV Use /")

z = input("Enter Your Operater : ")

result = child2()

if z == "+":
    result.add(a,b)
elif z == "-":
    result.sub(a,b)
elif z == "*":
    result.mul(a,b)
elif z == "/":
    result.div(a,b)