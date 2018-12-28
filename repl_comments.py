
from hashlib import sha256
from typing import List, Any


## derived from
# https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py

comments = []
## password: simplicity
correct_password = "2ae0514924b1db04e8c45002326641b5e6c74f182288ae8702d5c7250374669e"


def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

def add_comments():
    i = 0
    while True:
        print("Enter comment (or exit with -1): ")
        comment = input()
        if comment == "-1":
            print("Exitted succesfully")
            break
        else:
            comments.append(comment)
            print("Comments:")
            for i in range(len(comments)):
                print(str(i + 1) + ". " + comments[i])

            i += 1
def main():
    print("Welcome! You have to login first.")
    while True:
        print("Please enter your password, so that we can understand it is YOU.")
        input_password = create_hash(input())

        if input_password == password:
            print("Access granted.")
            break
        else:
            print("Incorrect password. Access denied.")
            return

    add_comments()


