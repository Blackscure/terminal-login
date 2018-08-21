from db import users
from user import User

class Menu():
    def display_menu(self):
        command = ""
        while command != "q":
            command = input("Enter 'r' to register 'l' to login and 'q' to quit: ")
            if command == "r":
                self.register()
            elif command == "l":
                self.login()
            elif command == "q":
                print("programm quited!!")

    def register(self):
        name = input("enter your name: ")
        password = input("enter your password: ")

        id = len(users) + 1
        print(id)
         
        for user in users:
            current_person = users[user]
            if name == current_person.name:
                print("name exists")

        new_person = User(name,password,id)

        users[id] = new_person
        print(users[id])



    def login(self):
        name = input("enter login name: ")
        password = input("enter login password: ")

        for user in users:
            current_user = users[user]
            if name == current_user.name and password == current_user.password:
                    print("login successfully.", name)
                    return
        
        print('user doesent exist or wrong password')
        return
      



