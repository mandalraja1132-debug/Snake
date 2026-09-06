# # # # # a="Dear {}, You done a great job.\nHere ${} is your bonus"
# # # # b="Rudr"
# # # # b1=1000
# # # # c="riya"
# # # # c1=200
# # # # # print(a.format(c,c1))
# # # # # print(a)
# # # # print(f"Dear {b}, You done a great job.\nHere ${c1} is your bonus")
# # # # a="Coding in Python is fun"
# # # # count=0
# # # # i=0
# # # # while i<len(a):
# # # #     if (a[i].lower() in "aeiou"):
# # # #         count+=1
# # # #     i+=1
# # # # print(count)
# # # # def avg(a,b,c):
# # # #     d=(a+b+c)/3
# # # #     return d

# # # # fs=avg(23,34,66)
# # # # print(fs)
# # # # def add(a,b,c=20):
# # # #     return a+b+c

# # # # ik=add(9,3,3)
# # # # print(ik)
# # # # def greet(name,time):
# # # #     return f" hey! ,{name} ,good {time}. "
# # # # a=greet("raja","evening")
# # # # print(a)
# # # # a=lambda x,y: x+y
# # # # print(a(7,6))
# # # # def feb(n):
# # # #     if n==0 or n==1:
# # # #         return n
# # # #     return (n-2)+(n-1)

# # # # print(feb(0))
# # # # import math
# # # # print(math.sqrt(81))

# # # # a="raja is  very good  student"
# # # # print(a.find("  "))
# # # # def greet():
# # # #     print("Good morning")

# # # # greet()
# # # # def square(num):
# # # #     return num*num

# # # # print(square(13)) 
# # # # def fullname(firstname,lastname):
# # # #     print(f"{firstname} {lastname}")

# # # # fullname("Rajat","Dalal")
# # # # def perimeter(l,w=10):
# # # #     return 2*(l+w)
# # # # print(perimeter(12,7))
# # # # add = lambda a,b: a+b 
# # # # print(add(18,12))
# # # # Program to find square root of a number

# # # # num = float(input("Enter a number: "))

# # # # square_root = num ** 0.5

# # # # print("Square root of", num, "is", square_root)
# # # # def root(a):
# # # #     return a**0.5

# # # # print(root(789))
# # # # marks=[12,23,34,45,46]
# # # # print(marks[2:5])

# # # # marks=[12,"raja",23,21.4]
# # # # kat=[34,56.6,"naina"]
# # # # print(marks)
# # # # marks.extend(kat)
# # # # print(marks)
# # # # a=5
# # # # table=[]
# # # # for i in range(1,11):
# # # #     table.append(a*i)
# # # # print(table)
# # # # tup=(3,5,7,)
# # # # print(type(tup))
# # # # print(tup[2])
# # # # tup=(23,34,45)
# # # # a,b,c=tup
# # # # print(a,b,c)
# # # # tup=(2,5,6,8,2,3,3,9)
# # # # print(tup.index(3))
# # # # s={1,2,3,4,1,3}
# # # # print(s,type(s))
# # # # print
# # # # a=[12,34,56,78]
# # # # b=[12,56,65,33]
# # # # a.extend(b)
# # # # print(set(a))
# # # # fruits=["apple","orange","pineapple"]
# # # # # fruits[1]="banana"
# # # # # print(len(fruits))
# # # # l=[]
# # # # for i in range(1,11):
# # # #     l.append(i)
# # # # print(l)
# # # # print(l[-3:])/
# # # # l=[5,2,9,1,7]
# # # # l.sort()
# # # # print(l)
# # # # l.append(10)
# # # # # print(l)
# # # # tup=(12,17)
# # # # kit=list(tup)
# # # # kit[0]=13
# # # # print(kit[0])
# # # # print(tup[1])
# # # # lis=["alice","janvi","mudadt"]
# # # # # lis[1]="rohan"
# # # # # print(lis)
# # # # lis.insert(1,"rohan")
# # # # print(lis)
# # # # st={2,3,4,2,3,7,6,8,4,6,6,3,2}
# # # # st.add(5)
# # # # st.remove(3)
# # # # print(st)
# # # # a={12,23,13,14}
# # # # b={13,24,12,11}
# # # # print(a.union(b))
# # # # print(a.intersection(b))
# # # # print(a-b)
# # # # # print(a.difference(b))
# # # # student={
# # # # "" nam":"raj",
# # # # 
# # # # student={
# # # #     "name":"raj",
# # # #     "rolln":32,
# # # #     "age":12
# # # # }
# # # # print(student["name"])
# # # # student["age"]=13
# # # # student["city"]="mumbai"
# # # # print(student)
# # # # class employee:
# # # #     company="hp"
# # # #     def get_salary(self):
# # # #         return 34000
# # # # e=employee()
# # # # print(e.get_salary())
# # # # marks={"harry":34,"jack":45,"joe":39}
# # # # # print(marks["joe"])
# # # # # marks["harry"]=49
# # # # marks.pop("joe")
# # # # print(marks)
# # # # # print(marks.values())
# # # # table={i:i*i*i for i in range(1,11)}
# # # # print(table)
# # # # class employee:
# # # #     company="Deloitte"
# # # #     def __init__(self,name,salary,bond,company):
# # # #         self.name=name
# # # #         self.salary=salary
# # # #         self.bond=bond
# # # #         self.company=company

# # # #     def get_emp(self):
# # # #         return f"Name of the employee is {self.name} paid ${self.salary}.having bond of {self.bond} years. working at {self.company} "

# # # # e1=employee("Karan",23000,2,"TCS")
# # # # print(e1.get_emp())
# # # # print(e1.company)
# # # # print(dir(e1))

# # # # l=list(map(int,input("enter a numbers seperated by comma: ").split(",")))
# # # # s=set(l)
# # # # a=list(s)
# # # # # print(a)
# # # # dic={
# # # #     "Watch":4000,
# # # #     "TV":7000,
# # # #     "cooler":6000
# # # # }
# # # # item={
# # # #     "bed":40000,
# # # #     "sofa":10000,
# # # #     "table":15000
# # # # }
# # # # r=dic.update(item)
# # # # print(r)
# # # # # print({**dic,**item})
# # # # # l=list(dict)
# # # # class animal:
# # # #     location="Australia"
# # # #     def __init__(self,name):
# # # #         self.name=name
# # # #     def speek(self):
# # # #         print("genric animal sound")
# # # # class dog(animal):
# # # #     def speek(self):
# # # #         super().speek()
# # # #         print("woof")
# # # # a=dog("bruno")
# # # # a.speek()
# # # # # print(a.location)
# # # # class car:
# # # #     def drive(self):
# # # #         print("car is moving")
# # # # a=car()
# # # # a.drive()
# # # # class person:
# # # #     def __init__(self,name,age):
# # # #         self.name=name
# # # #         self.age=age
# # # #     # def hello(self):
# # # #     #     print(self.name)
# # # #     #     print(self.age)
# # # # a=person("karan",21)
# # # # print(a.name)
# # # # print(a.age)
# # # # class animal:
# # # #     def __init__(self,name):
# # # #         self.name=name
# # # #     def sound(self):
# # # #         print("some sound")
# # # # class dog(animal):
# # # #     def sound(self):
# # # #         super().sound()
# # # #         print("woof!")
    
    

# # # # a=dog("bruno")
# # # # # a.sound()
# # # # def decoraters(func):
# # # #     def wapper():
# # # #         print("im about to print")
# # # #         func()
# # # #         print("i have done")
# # # #     return wapper

# # # # f=decorater(say_hello)
# # # # # f()  
# # # # def repeat(n):
# # # #     def decorator(fun):
# # # #         def wrapper(a):
# # # #             for i in range(n):
# # # #                 fun(a)
# # # #         return wrapper
# # # #     return decorator
# # # # # @repeat(7)
# # # # def say_hello(a):
# # # #     print(f"hello {a}")
# # # # say_hello=repeat(3)(say_hello)

# # # # say_hello("harry")

# # # # while True:
# # # #     try:
# # #         # a=int(input("entre a number:"))
# # #         # b=int(input("enter a number:"))
# # # #         print(f"quetient is {a/b}")
# # # #     except ZeroDivisionError:
# # # #         print("no.cant be devided by zero")
# # # #     except ValueError:
# # # #         print("dont enter bad typecast")
# # # #     except Exception as e:
# # # # #         print("some error occured",e)
# # # # while True:
# # # #     a=int(input("enter a number:"))
# # # #     b=int(input("enter a number:"))
# # # #     if b==0:
# # # #         raise ValueError("enter no. greater than zero")
# # # #     print(f"{a/b}")


# # # # x=int(input("enter a number:"))
# # # # y=int(input("enter a number:"))
# # # # def dev(a,b):
# # # #     try:
# # # #         c=a/b
# # # #         print(c)
# # # #         return c
# # # #     except Exception as e:
# # # #         print(e)
# # # #         return None
# # # #     finally:
# # # #         print("program executed")

# # # # dev(x,y)

# # # # num=[2,4,6,8,10]
# # # # # def square(x):
# # # # #     return x*x
# # # # new=tuple(map(lambda x:x*x,num))
          
# # # # print(new)
# # # # def _check(x):
# # # #     if x<9:
# # # #         return True
# # # #     else:
# # # #         return False

# # # # # a=[12,3,15,4,16,1,5,7,11,82,1,9,19]
# # # # # new=list(filter(_check,a))
# # # # # print(new)
# # # # a=list(map(int,input("enter :").split(",")))
# # # # new=list(filter(_check,a))
# # # # b=list(map(lambda x:x*x,new))
# # # # print(new)
# # # # print(b)
# # # from functools import reduce
# # # # num=[2,3,4,5]
# # # # def add(a,b):
# # # #     return a+b
# # # # c=reduce(add,num)
# # # # print(c)
# # # # def slow():
# # # #     print("very slow")
# # # #     print("very slow")
# # # #     print("very slow")
# # # #     print("very slow")
# # # #     print("very slow")
# # # #     print("very slow")
# # # #     print("very slow")
# # # #     return 70
# # # # if ((a:=slow())>10):
# # # #     print(a)
# # # # else:
# # # #     print("it not grater than ten")
# # # # while(dt:=input("enter a value")):
# # # #     print(dt)
# # # #     if dt=="R":
# # # #         break
# # # # def sum(*args):
# # # #     # print(args)
# # # #     total=0
# # # #     for i in args:
# # # #         total+=i
# # # #     return total




# # # # print(sum(11,23,34))
# # # # # print(c)
# # # # def multi(*args):
# # # #     product=1
# # # #     for i in args:
# # # #         product*=i
# # # #     return product
# # # # print(multi(2,3,4))
# # # # def marks(**kwargs):
# # # #     for i in kwargs.keys():
# # # #         print(f"marks of {i} is {kwargs[i]}")


# # # # marks(raj=20,sohit=40,mohit=50)
# # # # def st(*args,**kwargs):
# # # #     print(args)
# # # #     print(kwargs)

# # # # st(2,3,4,shu=30,rj=39,rk=88)
# # # # def decorater(func):
# # # #     def wapper():
# # # #         print("proggram started!")
# # # #         func()
# # # #         print("program ended")
# # # #     return wapper

# # # # @decorater
# # # # def say_hello():
# # # #     print("Hello!")
# # # # # f=decorater(say_hello)
# # # # # f()
# # # # say_hello()

# # # # from time import time
# # # # def decorator(func):
# # # #     def wapper(n):
# # # #         t1=time()
# # # #         func(n)
# # # #         t2=time()
# # # #         print(t2-t1)
# # # #     return wapper

# # # # @decorator
# # # # def sum(n):
# # # #     total=0
# # # #     for i in range(1,n+1):
# # # #         total+=i
# # # #     print(total)
  

# # # # a=sum(100000)
# # # # print(a)
# # # # a=[1,2,3,4,5]
# # # # b=list(map(lambda x:x**3,a))
# # # # print(b)
# # # # a=[10,11,12,13,14]
# # # # b=list(filter(lambda x:x%2==0,a))
# # # # print(b)
# # # # a=[1,2,3,4]
# # # # def product(a,b):
# # # #     return a*b
# # # # b=reduce(product,a)
# # # # print(b)
# # # # while (a:=input("enter somthing")):
# # # #     print(a)
# # # #     if a=="quit":
# # # #         break
    
# # # # a=["Python","rocks","ai"]
# # # # # def store():
# # # # #     for i in range(a):
# # # # #         a:
# # # # b=[w for i in a if ((w:=len(i))>4)]

# # # # print(b)
# # # # def sum(*args):
# # # #     total=0
# # # #     for i in args:
# # # #         total+=i
# # # #     return total
# # # # print(sum(13,24,27,33,98))

# # # # def val(**kwargs):
# # # #     for key,value in kwargs.items():
# # # #         print(f"{key}-{value}")
# # # #         # print(f"{i}-{kwargs[i]}")
# # # #         # print(f"{i}-{kwargs[i]}")
# # # # print(val(name="raman",age=32,city="kanpur"))

# # # # arr1=([2,4,6])
# # # # arr2=([3,5,4])
# # # # # result=[]
# # # # # for i in range(len(arr1)):
# # # # #     result.append(arr1[i]+arr2[i])
# # # # # print(result)
# # # # # import numpy as np
# # # # # sum=np.array(arr1)*np.array(arr2)
# # # # # print(sum)
# # # # result=[]
# # # # for i in range (len(arr1)):
# # # #     result.append(arr1[i]*arr2[i])
# # # # print(result)
# # # # print(type(result))
# # # # a=[2,4,6]
# # # # b=[3,5,7]
# # # # result=[]
# # # # for i in range(len(a)):
# # # #     result.append(a[i]+b[i])
# # # # print(result)
# # # # a=int(input("enter a no."))
# # # # b=a**(1/2)
# # # # print(b)
# # # # import math
# # # # a=int(input("enter: "))
# # # # c=math.sqrt(a)
# # # # print(c)

# # # # h=int(input("enter "))
# # # # b=5
# # # # # area=(h*b)/2
# # # # # print(area)
# # # # # c=h
# # # # # h=b
# # # # # b=c
# # # # # print(b)
# # # # # print(h)
# # # # if h>0:
# # # #     print("+ve")
# # # # elif h<0:
# # # #     print("-ve")
# # # # else:
# # # #     print("0")
# # # # import array as arr
# # # # myarr=arr.array('b',[])
# # # # n=int(input("limit of array: "))
# # # # for i in range(n):
# # # #     x=int(input("enter a number: "))
# # # #     myarr.append(x)
# # # # print(myarr)
# # # # a=int(input("enter: "))
# # # # if (a%4==0) and(a%100!=0):
# # # #     print("leap")
# # # # elif (a%400==0)and(a%100==0):
# # # #     print("leap")
# # # # else:
# # # #     print("common")

# # # # a,b,c=map(int,input("enter no. : ").split(","))
# # # # if a>b and a>c:
# # # #     print( a , "ia greatest")
# # # # elif b>a and b>c:
# # # #     print(b, "is greatest")
# # # # else :
# # # #     print( c, " is greatest")
# # # # profession=input("enter profession : ")
# # # # print("yes") if profession=="Engineering" else print("no")
# # # # num=int(input("enter a no. "))
# # # # if  num<=1:
# # # #     print("not prime")
# # # # else:
# # # #     for i in range (2,num):
# # # #         if num%i==0:
# # # #             print("not prime")
# # # #             break
# # # #     else:
# # # #         print("prime")

# # # # import random
# # # # num=random.randint(1000,9999)
# # # # # print(num)
# # # # a=int(input("enter a number: "))
# # # # b= int(input("enter a number : "))
# # # # for i in range (a,b+1):
# # # #     if i <=1 :
# # # #         print("error")
# # # #     else :
# # # #         for j in (2,i):
# # # #             i%j!=0
# # # #             print(i)
# # # # a=int(input("enter number :"))
# # # # # def ferehite(n):
# # # # #     print(n*33.3)
# # # # # ferehite(a)
# # # # # fact=1
# # # # for i in range(1,11):22
# # # # #     n=a*i
# # # # #     print(n)
# # # # n=int(input("enter a number: "))
# # # # f=str(n)
# # # # i=len(f)
# # # # a=n
# # # # sum=0
# # # # while n>0:
# # # #     r=n%10
# # # #     c=r**i
# # # #     sum+=c
# # # #     t=n//10
# # # #     n=t
# # # # if sum==a:
# # # #     print("Armstrong")
# # # # else:
# # # #     print("NOt")

# # # # a,b=int(input("enter a no.: ")),int(input("enter a no.: "))
# # # # lis=[]
# # # # count=0
# # # # for i in range(a,b+1):
# # # #     total=0
# # # #     length=len(str(i))
# # # #     temp=i
# # # #     while temp>0:
# # # #         r=temp%10
# # # #         total+=r**length
# # # #         temp//=10
        
# # # #     if total==i:
# # # #         lis.append(i)
# # # #         count+=1
# # # # print(count)
# # # # print(lis)
# # # # n=int(input("enter a num: "))
# # # # # if n>0:
# # # # #     sum=0
# # # # #     for i in range(1,n):
# # # # #         sum+=i
# # # # #     print(sum)
# # # # # else:
# # # # #     print("enter value > 0")
# # # # def square(x):
# # # #     return lambda x:x*x
    


# # # # print(square(n))
# # # n=int(input("enter n terms: "))
# # # # lis=list(map(int,input("enter numbers :").split(",")))
# # # # sq=list(map(lambda x:x*x,lis))
# # # # # print(sq)
# # # l=[12,23,34,56,67,78,89,90,22]
# # # lis=list(filter(lambda x:x%n==0,l))
# # # for i in lis:
# # #     print(i)
# # # a=str(input("enter a num :"))
# # # print(ord(a))
# # # def hcf(x,y):
# # #     a=[]
# # #     if x>y:
# # #         smaller=y
# # #         bigger=x10
# # #     else:
# # #         smaller=x
# # #         bigger=y
    
# # #     for i in range(1,smaller):
# # #         if smaller%i==0 and bigger%i==0:
# # #             a.append(i)
# # #     print(a[-1])

# # # hcf(12,15)
# # n= int(input("enter a num: "))
# # o=str(input("enter a operator: "))
# # m= int(input("enter a num: "))
# # # for i in range(1,n+1):
# # #     if n%i==0:
# # #         print(i)


# # if o=="+":
# #     print(n+m)
# # elif o=="-":
# #     print(n-m)
# # elif o=="*":
# #     print(n*m)
# # elif o=="//":
# #     print(n//m)
# # else :
# #     print("enter valid operator")
# # import calendar
# # a=int(input("enter year: "))
# # b= int(input("enter month: "))
# # cal=calendar.month(a,b)
# # print(cal)
        

# # def lenth(a):
# #     return len(a)

# n=["mohan","rajiv","ruhi","shila"]
# # print(lenth(n))

# # def line(a):
# #     b=""
# #     for i in a:
# #         b+=i
# # #         b+=" "
# # #     return b

# # print(line(n))
# # def line(a):
# #     return " ".join(a)
# # print(line(n))

# # def check(n):
# #     if n==0:
# #         return
# #     print (n)
# #     check(n-1)
    

# # check(6)
# # def fact(n):
# #     fac=1
# #     if n==1:
# #         return fac
# #     else:
# #         return n*fact(n-1)
# # def sum(n):
# #     if n==0:
# #         return 0
# #     else:
# #         return n+sum(n-1)
    
# # print(sum(6))
# def lis(a):
#     if a==0:
#         return 
#     else:
#         return lis(a%2)


# lis(10)

# def binary(n):
#     if n>1:
#         binary(n//2)
#     print(n%2,end="")

# binary(10)   
        
# def sum(n):
#     if n>1:
#         sum(n-1)
#     return n+n

# print(sum(6))
# import numpy as np
# arr1=np.array([[12,13,14],[11,10,9]])
# arr2=np.array([[8,9,7],[2,5,6]])
# a=sum(arr1+arr2)
# print(a)

# def check(a):
#     b=a[::-1]
#     if b==a:
#         print("palindrom")
#     else:
#         print("not")

# check("maah")


# t1=[[2,3,4],[9,7,8]]
# # t2=[[0,0],
# #     [0,0],
# #     [0,0]]
# # # for i in range(len(t1)):
# # #     for j in range(len(t1[0])):
# # #         t2[j][i]==t1[i][j]
# # # for i in t2:
# # #     print(i)
# t2=[[t1[j][i] for j in range(len(t1))]for i in range(len(t1[0])) ]
# for i in t2:
#     print(i)

# a="Th!ara@ b!ahi* j)og%&nda$r"
# c="!@#$%^&*()"
# b=""
# for i in a:
#   if i not in c:
#     b+=i
# print(b)

# a=[[2,3,4],
#    [5,6,7],
#    [8,9,1]]
# b=[[4,7,9],
#    [2,5,8],
#    [1,6,3]]
# c=[[0,0,0],
#    [0,0,0],
#    [0,0,0]]
# for i in range(len(a)):
#   for j in range(len((a)[0])):
#     for k in range(len(b)):
#         c[i][j]+=a[i][k]*b[k][j]
# for i in c:
#   print(i)

# a="Prime Minister of India is shri Narendra Modi"
# b=a.split()
# for i in range(len(b)):
#     b[i]=b[i].lower()
# print(b)
# b.sort()
# print(" ".join(b))

# a={2,3,4,5,7}
# b={4,8,0,9,2,3}
# c=a.symmetric_difference(b)
# print(c)

# a=input("write a sentence: " )
# b=a.lower()
# c="aeiou"
# count=0
# for i in b:
#     for j in c:
#         if i==j:
#             count+=1
# print(count)

# import PIL
# from PIL import Image

# # img=PIL.Image.open("C:/Users/91879/Pictures/Screenshots/Screenshot 2026-07-27 221116.png")
# # a,b=img.size
# # print(a,"X",b)
# # dict={"JHON":37,"Madro":22}
# # dict1={"Mohit":40,"JHON":37}
# # b=(dict|dict1)
# # print(b)
# # print(dict)
        
# # a=[12,3,4,56,67,78,23,45,56,7,8]
# # for i ,v in enumerate(a):
# # #     print(i,v)
# # a=[12,3,4,56,67,78,23,45,56,7,8]
# # for i in range(len(a)):
# #     print(i," ",a[i])

# a={
#     "raj":34,
#     "sumit":55,
#     "minal":23
#     }
# for key ,value in a.items():
#     print(key," ",value)

# b=sorted(a.items(),lambda x:x[1])
# print(b)
# c=sorted(a.values())
# print(c)

# import re
# text="quick brown fox jumped over the lazy brown dog."
# # match=re.findall("brown",text)
# # print(match)
# # if match :
# #     print("match foud")
# #     # print("Start index", match.start())
# #     # print("end index ", match.end())
# new_text=re.sub("fox","cat",text)
# # print(new_text)
# def greet(name="friend"):
#     print(f"Hello, {name}! Welcome!")
try:
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))
    print("what kind of operation you want to perform: + for addition \n, - for subtraction \n, * for multiplication \n, / for division")
    c=input("enter a operator: ")
    match c:
        case "+":
            print(f"sum of {a} and {b} is {a+b}")
    match c:
        case "-":
            print(f"difference between {a} and {b} is {a-b}")
    match c:
        case "*":
            print(f"Prduct of {a} and {b} is {a*b}")
    match c:
        case "/":
            print(f"Division of {a} and {b} is {a/b}")
        case default:
            print(f"There is an error check numbers {a},{b} or the operator {c}")

except Exception as e:
    print("enter valid number",e)


