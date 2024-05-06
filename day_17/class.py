class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username= username
        self.followers= 0
        self.followings=0
    def follow(self, user):
        user.followers+=1
        user.followings+=1

        print("New user being created....")

user_2 = User("002","Angela")
user_1 = User("001","Aviram")
user_1.follow(user_2)
# user_2.follow(user_1)
print(user_1.followers)
print(user_1.followings)
print(user_2.followers)
print(user_2.followings)
# print(user_1.follow)

# user_1.user_name= "Aviram"
# print(user_1.user_name)

# class MyCar:
#    def __init__(self,seats):
#       self.seats= seats