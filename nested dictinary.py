# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
# for p_id, p_info in people.items():
#     print("\nPerson ID:", p_id)
#     for key in p_info:
#         print(key + ':', p_info[key])

# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
#           3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
#           4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}
# del people[3], people[4]
# print(people)


# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
#           3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
#           4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}
# del people[3]['married']
# del people[4]['married']
# print(people[3])
# print(people[4])


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
        2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(people[2]['name'])
print(people[1]['age'])
print(people[1]['sex'])



# D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#      'emp2': {'name': 'Kim', 'job': 'Dev'},
#      'emp3': {'name': 'Sam', 'job': 'Dev'}}
# for id, info in D.items():
#     print("\nEmployee ID:", id)
#     for key in info:
#         print(key + ':', info[key])


# myfamily = {
# "child1" : {
# "name" : "Emil",
# "year" : 2004
# },
# "child2" : {
# "name" : "Tobias",
# "year" : 2007
# },
# "child3" : {
# "name" : "Linus",
# "year" : 2011
# }
# } 
# print(myfamily)


# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# } 
# print(child1,child2,child3)




# mydict = {'name': 'John', 'age': 45, 'gender': 'male'}
# for k, v in mydict.items():
#     print("key =", k)
#     print("value =", v) 



