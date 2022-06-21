dict1={1:3,2:3,5:6,7:8,9:11,87:90,48:89}
i=0
count=1
for i in dict1:
    if (dict1[i]%2==0):
        count=count+1
    if (count==2):
        print(i,"it is prime no")
    else:
        print(i,"it is not a prime no")