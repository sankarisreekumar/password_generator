import random

chars="bcdefghjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"

while 1:
    password_len=int(input("what length would you like your password to be:"))
    password_count=int(input("How many password would you like:"))
    for x in range(0,password_count):
        password=""
        for x in range(0,password_len):
            password_char=random.choice(chars)
            password =password+password_char
        print("here is your password:",password)