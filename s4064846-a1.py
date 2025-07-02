import hashlib

def question1():
    # Step 1: Take an arbitrary string as input from the user.
    user_input = input("Enter a string: ")

    # Step 2: Computes and displays its hash.
    # Create a new hash object using sha256 which is used by Bitcoin
    hash = hashlib.sha256() 

    # Update the hash object with our user input
    hash.update(user_input.encode('utf-8'))

    # Display the hash in hex format
    print(hash.digest())

    # Step 3: Demonstrate the avalanche effect by reversing first and last character
    modified_input = user_input[-1] + user_input[1:-1] + user_input[0]

    modified_hash = hashlib.sha256()
    modified_hash.update(modified_input.encode('utf-8'))

    print(modified_hash.digest())

    # Highlight the difference between the two hashes


    # Return hash value for use in pre-image testing
    return hash

question1()