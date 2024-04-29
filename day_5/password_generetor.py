# import random
# alphabet= "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
# Alphabets= alphabet.split()
# numbers="1 2 3 4 5 6 7  9 0"
# Num= numbers.split()
# characters="! @ # $  % ^ & * ~ ' < ? > _ - , . / \ | " 
# char=characters.split()
# pick=[Alphabets,Num,char]
# password1=''
# password2=""
# password3=''
# print()
# print("Welcome to password generator!")
# n_letters=int(input("Enter the number of alphabets you want:-  ")) 
# n_symbols= int(input("how many symbols you want:-    "))
# n_numbers= int(input("how many numbers you want:-    "))
# for i in range(0,n_letters):
#      randum_alphabet=random.choice(Alphabets)
#      password1 += randum_alphabet
# for i in range(0,n_numbers):
#      random_num=random.choice(Num)
#      password2 += random_num
# for i in range(0,n_numbers):
#      random_char=random.choice(char)
#      password3 += random_char
# print("Your ai generated password is ", password1+password2+password3)





# very random


import random
alphabet= "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
Alphabets= alphabet.split()
numbers="1 2 3 4 5 6 7  9 0"
Num= numbers.split()
characters="! @ # $  % ^ & * ~ ' < ? > _ - , . / \ | " 
char=characters.split()
pick=[Alphabets,Num,char]
password_list= []
print()
print("Welcome to password generator!")
n_letters=int(input("Enter the number of alphabets you want:-  ")) 
n_symbols= int(input("how many symbols you want:-    "))
n_numbers= int(input("how many numbers you want:-    "))
for i in range(0,n_letters):
     randum_alphabet=random.choice(Alphabets)
     password_list += randum_alphabet
for i in range(0,n_numbers):
     random_num=random.choice(Num)
     password_list += random_num
for i in range(0,n_numbers):
     random_char=random.choice(char)
     password_list += random_char
total_number=n_letters+n_numbers+n_symbols
random.shuffle(password_list)
password=''
print(password_list)
for char in password_list:
   password += char
print(password)
