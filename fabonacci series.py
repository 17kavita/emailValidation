n=int(input("enter the number:-"))
a=0
b=1
c=0
# print(a)
# print(b)
i=1
while i<n:
    c=a+b
    a=b
    b=c
    i=i+1
    # print(c)
print("the fibonacci no:-",c)
