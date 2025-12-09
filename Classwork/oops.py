# class Student:
#     roll_number = 3 #class variable

#     def __init__(self,roll_number):
#         self.roll_number = roll_number #instance variable

#     def learn(self): #class method
#         return "Learning..."
#     def bunk():
#         pass

# #making a object and assigning a variable to it
# Visal = Student(157)
# print(Visal.roll_number)
# print(Visal.learn())

# print(Student.roll_number)

# class Faculty:
#     pass

# prasad = Faculty()
# prasad.skills = ["python","js"]
# print(prasad.skills)

# gatik = Faculty()
# Faculty.skills = ["read"]
# print(gatik.skills)


# def teach():
#     return "teaching"

# prasad = Faculty()
# prasad.teach = teach
# print(prasad.teach()) 

# #Parent class
# class Person:
    
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def print_fullname(self):
#         return self.fname + " " + self.lname
# #Child class    
# class User(Person):  
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#         # self.fname = fname
#         # self.lname = lname

#     #from parent - overrides parent function
#     def print_fullname(self):
#         return self.fname + " and " + self.lname
    
#     #it's own
#     def set_username(self):
#         return self.fname



# # make object of Person class
# user_one = User("Aareen", "Dakway")
# print(user_one.fname)
# print(user_one.lname)

# # make object of user class
# user_one = User("Aareen", "Dakway")
# print(user_one.fname)
# print(user_one.lname)
# print(user_one.print_fullname())


#User authentication system

user_input = input("Enter username: ")
user_password = input("Enter password: ")

class user:
    def __init__(self, username, password):
        self.username = username
        self.__password = password #Password is private
    
    def get_password(self):
        return self.__password

class Auth(user):
    def __init__(self,username,password):
        super().__init__(username,password)

    def login(self,username,password):
        if username == user_input and self.get_password() == user_password:
            return True 
        else:
            return False 
    def reg():
        pass


object = Auth('Aareen','nigga')
print(object.login(user_input,user_password))

#Abstraction
# from abc import ABC,abstractmethod

# class Human(ABC):
#     @abstractmethod
#     def talk(self):
#         print("talking..")

# class Man(Human):

#     # def talk(self):
#     #     print('hmmmmm')

#     def walk(self):
#         print("walking")
    
# person = Man()
# person.talk()