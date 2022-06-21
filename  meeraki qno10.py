di= {
'Alex': ['subj1', 'subj2', 'subj3'], 
'David': ['subj1', 'subj2']}
# print(di.count("Alex",'David'))

sum=0
for i in di:
    sum+=len(di[i])
print(sum)