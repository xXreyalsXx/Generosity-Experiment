# imports
import pickle
import random

# defining user number
user_number = 0

# creating UserInfo dictionary
UserInfo = {
}

# user IDs list
user_IDs = [0, ]

# user_coins variable
user_coins = 0

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

# hashing information
hashed_password = hash(password)
hashed_user_ID = hash(user_ID)
hashed_username = hash(username)

# user info nested dictionaries
user_number += 1
UserInfo[user_number] = {'username': hashed_username, 'password': hashed_password, 'user_ID': hashed_user_ID, 'user_number': user_number}

# downloading UserInfo
with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(UserInfo, f)
