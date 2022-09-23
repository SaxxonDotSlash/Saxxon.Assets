#no sql database. python version 1

users = ['admin', 'test', 'empty']
passwd = ['Secure-password1', 'password1', 'empty']

print(users)
print(passwd)

eid = input("Enter your username: ")

if eid in users :
    print("Welcome " + eid + ". Please enter your password.")
    epass = input("Enter your password: ")
