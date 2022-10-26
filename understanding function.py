# def add():
#     a=5
#     b=7
#     sum=a+b
#     return sum
# print(add())
# def add(a,b):
#     s=a+b
#     print(s)
# add(5,6)
# def add():
#     print("enter two number")
#     a=int(input())
#     b=int(input())
#     s=a+b
#     return s
# print(add())
# def add(a,b):
#     s=a+b
#     return s
# print(add(2,4))



# def f1():
#     print("hello")
# x=f1()
# print(x,"   ",type(x))
# # when function return nothing it return none
# def sum(a,b,c=0):
#     s=a+b+c
#     print(s)
# sum(10,20)
# sum(10,20,98)
# c=0 has default argument
# def sum(a,b=0,c=0):
#     s=a+b+c
#     print(s)
# sum(10)
# sum(10,20,30)
# def sum(a=0,b=0,c=0):
#     s=a+b+c
#     print(s)
# sum()
# sum()


# def sum(a=0,b,c=0)....error
# def sum(a=0,b=0,c=0).....no error
# def sum(a,b=0,c=0)......no error
# def sum(a=0,b=0,c)......error
# def f(a,b):
#     print("a=",a,"b=",b)
# f(10,20)
# f(30,39)
# # f(b=90,a=5).....not change position
# f(8,b=90)





# variable length argument
# def avg(a,b):
#     return(a+b)/2
# print(avg(10,30))
# def avg(*n):
#     s=0
#     for x in n:
#         s=s+x
#     return s/len(n)#error for emipty element
# x=avg(10,20,30)
# print(x)
# def avg(*n):
#     s=0
#     for x in n:
#         s=s+x
#     if len(n)!=0:
#         return s/len(n)#no for emipty element
#     else:
#         return "no element"
# x=avg(9,5,6,4,3,2,2,3)
# print(x)
# def avg(*n):
#     s=0
#     for x in n:
#         s=s+x
#     if len(n)!=0:
#         return s/len(n)#no for emipty element
#     else:
#         return "no element"
# x=avg(9,5,6,4,3,2,2,3)
# print(x)





# def f(*points,playername):
#     print(playername,end=" ")
#     s=0
#     for x in points:
#        s=s+int(x)
#     print("tatal points=",s)
# f(10,11,9,playername="vikash")
# f(10,11,9,4,playername="gudiya")






# *n.....Tuple
# **n....Dictionary
# def f(**k):
#     # print("name")
#     for key,value in k.items():
#         print(key,"-",value)
# f(name="sammer",age=32)
# f(name="hfjh",age=34)
