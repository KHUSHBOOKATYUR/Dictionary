# details={
# "name":"Shanti",
# "age":12,
# "email":"shanti@navgurukul.org",
# }
# print(details["name"])
# print(details["age"])
# print(details["email"])


# c=dict()
# for i in range(1,16):
#     c=i*i
#     print(c)


# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)



# n=[50,40,23,70,56,12,5,80,15,10,7]
# i=0
# max=0
# while i<len(n):
#     if n[i]>max:
#         max=n[i]
#     i=i+1
# print(max)

a=[1,1,0,1,1,1,0,1]
i=0
k=[]
count=0
while i<len(a):
    count=count+a[i]
    k.append(count)
    i=i+1
print(k)
# print(count)