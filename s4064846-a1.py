import hashlib

def question1():
    # Step 1: Take an arbitrary string as input from the user.
    user_input = input("Enter a string: ")

    # Step 2: Computes and displays its hash.
    # Create a new hash object using sha256 which is used by Bitcoin
    hash = hashlib.sha256() 

    # Update the hash object with our user input
    hash.update(user_input.encode('utf-8'))

    # Step 3: Demonstrate the avalanche effect by flipping a single bit
    
    # Convert user_input to binary 
    # Source: https://www.geeksforgeeks.org/python/python-convert-string-to-binary/
    binary_input = ''.join(format(ord(char), '08b') for char in user_input)

    print("\nFlipped string: ", binary_input)
    
    # Flip the first bit
    first_bit = binary_input[0]

    if first_bit == '0':
        binary_input = '1' + binary_input[1:]
    else:
        binary_input = '0' + binary_input[1:]
    
    print("Unflipped string: ", binary_input)

    # Convert the binary string into an encoded, hashable string
    # Source: https://stackoverflow.com/questions/32675679/convert-binary-string-to-bytearray-in-python-3
    modified_input = int(binary_input, 2).to_bytes((len(binary_input) + 7) // 8)

    # Create the new hash
    modified_hash = hashlib.sha256()
    modified_hash.update(modified_input)
    
    # Highlight the difference between the two hashes
    hash_digest = hash.hexdigest()
    modified_digest = modified_hash.hexdigest()
    
    print("\nOld Hash: " + hash_digest)
    print("New Hash: " + modified_digest)

    # Convert both hashes into binary format
    LENGTH = 256

    # Use .digest() method here for accuracy
    binary_hash = ''.join(format(ord(char), '08b') for char in hash.digest())
    binary_modified = ''.join(format(ord(char), '08b') for char in modified_hash.digest())

    # XOR the hashes to look for differences
    xor_string = ''
    flipped_bits = 0

    for i in range(LENGTH):
        current = str(int(binary_hash[i]) ^ int(binary_modified[i]))
        xor_string += current

        if current == '1':
            flipped_bits += 1
    
    print(flipped_bits)
    avalance_effect = flipped_bits / LENGTH
    print("Avalance Effect = ", avalance_effect)

    # Return hash value for use in pre-image testing
    return hash

question1()