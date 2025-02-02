'''
class User: #Class name should be in Pascal case
    pass

user1=User()
user1.id='001'
user1.username = 'Masoooooom'

print(user1.username)


user2=User()
user2.id='002'
user2.name = 'jack'
'''
#consructor

class User:
    def __init__(self,user_id,username):
        print('New User Created')
        self.id=user_id
        self.username = username
        self.followers=0
        self.following=0
        #Adding method to a class
        def follow(self,user):
            user.followers+=1
            self.following+=1



user1=User('001',"Masoom")

user2=User('002',"Raza")
print(user1.id)
print(user1.username)
print(user2.id)
print(user2.username)
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)