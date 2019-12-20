class User:
    login: str
    age: int
    __password: str = "123123"
    role = "user"

    def __init__(self, new_login: str):
        self.age = 0
        self.login = new_login

    def info(self):
        print(self.__password)



class SuperUser(User):
    role = "admin"

    def info(self):
        super(SuperUser, self).info()
        print("!!!")

user1 = User("password")
user1.__password = "456"
print(user1.__password)
user1.info()
# print(user1.age)
# print(user1.login)
# print(user1.role)

user2 = SuperUser("admin_password")
# user2.info()
# print(user2.age)
# print(user2.login)
# print(user2.role)