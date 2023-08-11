# Secure Python Password Authentication

import getpass
# Simulating a database of usernames and passwords

db = {"tech.twitts": "789@123", "thomas.henry": "657@908"}

user= input("Enter Your Username: ")
password = getpass.getpass("Enter Your Password: ")
for i in db.keys():
  if user == i:
    while password!= db.get(i):
        password = getpass.getpass("Wrong password. Try again: ")
    break;
print("Verified! You're in!")
