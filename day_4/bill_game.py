import random
names= input("name of your 5 fiends - ")
list= names.split()
c=len(list)
pick=random.randint(0,c-1)
print(list[pick])