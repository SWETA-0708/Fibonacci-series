
# t=int(input("enter the limit"))
# n1,n2=0,1
# count=0
# if t<=0:
#     print("please enter a positive number")
# elif t==1:
#     print("Fibonacci sequence upto",n,":")
#     print(n1)
# else:
#     print("Fibonacci sequence:")
#     while count<t:
#         print(n1)
#         n=n1+n2
#         n1=n2
#         n2=n
#         count +=1
t=int(input("enter the limit"))
a=0
b=1

print("fibonacci series:","\n",a,"\n",b,"\n", end=" ")
for i in range(2,t):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    


    print()
