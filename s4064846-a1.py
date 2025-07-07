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
    print(hash.hexdigest())

    # Step 3: Demonstrate the avalanche effect by flipping a single bit
    # Convert user_input to binary (https://www.geeksforgeeks.org/python/python-convert-string-to-binary/)
    binary_input = ''.join(format(ord(char), '08b') for char in user_input)

    print("Flipped string: ", binary_input)
    # Flip the first bit
    first_bit = binary_input[0]

    if first_bit == '0':
        binary_input = '1' + binary_input[1:]
    else:
        binary_input = '0' + binary_input[1:]
    
    print("Unflipped string: ", binary_input)

    modified_hash = hashlib.sha256()

    # Update the hash object with our user input
    # modified_hash.update(modified_input.encode('utf-8'))

    # print(modified_hash.hexdigest())

    # Highlight the difference between the two hashes
    

    # Return hash value for use in pre-image testing
    return hash

question1()