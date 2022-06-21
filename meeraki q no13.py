dict = {
'a':50, 
'b':58,
'c': 56,
'd':40,
'e':100, 
'f':20}
k=[]
max=0
for x in range(2):
    for j in dict[x]:
        if dict[x][j]>max:
            max=dict[i][j]
        k.append(max)
print(k)


# a=[5,-1,3,4,2,0,-6]
# i=0
# k=[]
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     k.append(sum)
#     i=i+1
# print(k)
