num= int(input ("Enter a number:  "))
def check(num):
    prime=True
    for n in range (2,num):
          if num %n==0 :
            prime=False
    if prime==True:
        print("Prime number ")
    elif prime==False: 
        print("its not a prime number")
check(num)