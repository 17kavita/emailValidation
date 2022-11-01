num=int(input("enter the no:-"))

def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)

print(fact(num))