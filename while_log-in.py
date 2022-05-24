"""Creating and authentification of password"""

"""Creating of user acount"""

print("\tCrete your user account AR")
print("Create a user")
user=input(" Enter a username: ")
print("Create a password. ")
create=input(" Enter a password: ")
print("Confirm password.")
password=input(" Enter your password: ")

if not password == create:
    while not password == create:
        print("Password incorrect.")
        password = input(" Enter your password: ")
        if password == create:
            print("Password correct. \n")
else:
    print("password correct. \n")
password=create

"""Test of authentication: """

print("\tLong in")
open_usr=input("Username: ")
if not open_usr == user:
    while not open_usr == user:
        print("Username not found or incorrect")
        open_usr = input("Enter your Username again: ")
        if open_usr == user:
            print("Username correct \n")

open_pss=input("Password: ")
if not open_pss == password:
    while not open_pss == password:
        print("Password incorrect.")
        open_pss=input("Enter your password again: ")
        if open_pss == password:
            print("password correct.")
            print("Welcome to AR...")
else:
    print("Welcome to AR")