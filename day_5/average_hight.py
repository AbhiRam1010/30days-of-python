students_height= input("input list of student heights ").split()
for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])
print(students_height)
height=0
max=0
num=len(students_height)
for k in range(0,num-1):
    if students_height[k]>=students_height[k+1]:
       max= students_height[k]
    elif students_height[k]<=students_height[k+1]:
       max= students_height[k+1]
    height += students_height[k]  
    # height=height+students_height[k]
avg_height=height//num
print(max)
print(height)
print(avg_height)