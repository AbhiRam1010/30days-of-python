# year = int(input("Enter a year\t"))
# if(year%4==0):
#   if(year%100==0):
#     if(year%400==0):
#      print("its a leap year")
#     else:
#         print("not a leap year")
#   else:
#     print("its a leap year")
# else:
#     print("Its not a leap year")

def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
    print(n+1)

show(3)
