# a = {(1,2):1,(2,3):2}
# print(a[1,2])

# a = {(1,2):1,(2,3):2}
# print(a[1,2])


# fruit = {}

# def addone(index):
#     if index in fruit:
#         fruit[index]=1
#     else:
#         fruit[index]= 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print(len(fruit))
# print(fruit)


# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print(len(Details["Student"])) 



# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)

# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec
# rec = {
# "Name" : "Python", 
# "Age":"20", 
# "Addr" : "NJ", 
# "Country" : "USA"
# }
# id2 = id(rec)
# print(id1 == id2)


# a = "1C0C1C1A0Bi"
# a_bytes = bytes(a, "ascii")
# print(' '.join(["{0:b}".format(x) for x in a_bytes]))


# import math
# def toBinary(a):
#   l,m=[],[]
#   for i in a:
#     l.append(ord(i))
#   for i in l:
#     m.append(int(bin(i)[2:]))
#   return m

# print("''Hello world'' in binary is ") 
# print(toBinary("1c0c1c1aobi"))


# m=int(input("enter the number"))
# n=int(input("enter the number"))
# sum1=0
# sum2=0
# for i in range(n):
#     if i%n==0:
#         sum1+=i
#     else:
#         sum2+=i
# print(abs(sum2-sum1))



# rat count house:
# def fun(r,unit,arr,n):
#     if n==0:
#         return -1
#     total=r*unit
#     food=0
#     house=0
#     for house in range(n):
#         food+=arr[house]
#         if food >=total:
#             break
#     if total >food:
#         return 0
#     return house+1
# r=int(input())
# unit=int(input())
# n=int(input())

# arr=list(map(int,input().split()))
# print(fun(r,unit,arr,n))




# diffrence of sum1
# n=int(input())
# m=int(input())
# sum1=0
# sum2=0
# for i in range(1,m+1):
#     if i%n==0:
#         sum1+=i
#     else:
#         sum2+=i
# print(sum2-sum1)




# def fun(l, u, p, d ):
#     s =input("enter the name:-")
#     if (len(s) >= 5):
#         for i in s: 
#             if (i.islower()):
#                 l+=1        
#             if (i.isupper()):
#                 u+=1           
#             if (i.isdigit()):
#                 d+=1           
#             if(i=='@'or i=='$' or i=='_'):
#                 p+=1           
#     if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
#         print(u)
#         return True
#     else:
#         print("Invalid Password")
# fun(0,0,0,0)



# Password Checker 11
# def CheckPassword(s,n):
#     if n<4:
#         return 0
#     if s[0].isdigit():
#         return 0
#     cap=0
#     nu=0
#     for i in range(n):
#         if s[i]==' ' or s[i]=='/':
#             return 0
#         if s[i]>='A' and s[i]<='Z':
#             cap+=1
#         elif s[i].isdigit():
#             nu+=1
 
#     if cap>0 and nu>0:
#         return 1
#     else:
#         return 0
 
# s=input()
# a=len(s)
# print(CheckPassword(s,a))


    


# a=input("Enter string 1:")
# b=input("Enter string 2:")
# count=0
# for i in a:
#     for j in b:
#         if i==j:
#             count=count+1
# if count==len(a):
#     print("yes")
# else:
#     print("no")
           
  

