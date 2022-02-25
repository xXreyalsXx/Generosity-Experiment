# imports
import pickle
import random
import hashlib

# defining user number
user_number = 0

# creating UserInfo dictionary
UserInfo = {
}

# user IDs list
user_IDs = [0, ]

# user_coins variable
user_coins = 0


while 1 == 1:

    # getting username
    username = input("what would you like your username to be?: ")

    # password and password length
    password = input("what would you like your password to be?: ")
    while len(password) < 5:
        print("your password is too short")
        password = input("what would you like your password to be?: ")

    # rolling user ID
    user_ID = random.randint(1, 10000000000)

    # checking if user_ID is in user_IDs
    while user_ID in user_IDs:
        user_ID = random.randint(1, 10000000000)

    # appending list with new ID
    user_IDs.append(user_ID)

    # converting information from strings to bytes
    encoded_username = username.encode(encoding = 'UTF-8', errors = 'strict')
    encoded_password = password.encode(encoding = 'UTF-8', errors = 'strict')

    # hashing information
    hashed_username = hashlib.blake2b(encoded_username).hexdigest()
    hashed_password = hashlib.blake2b(encoded_password).hexdigest()

    # user info nested dictionaries
    user_number += 1
    UserInfo[user_number] = {'username': hashed_username, 'password': hashed_password, 'user_ID': user_ID, 'user_number': user_number, 'user_coins': user_coins}

    # downloading UserInfo
    with open('UserInfo.pkl', 'wb') as f:
        pickle.dump(UserInfo, f)
