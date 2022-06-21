a={'prime':20,'anjali':200,"khushbu":44,"kamini":56}
for i in a:
    for j in a:
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a,"its assending")