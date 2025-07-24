import hashlib
import string
import random

# Step 1: Take an arbitrary string as input from the user, converted to uppercase to regulate all strings
user_input = input("Enter a string: ").upper()

def question1(input):

    # Step 2: Compute and displays hash.
    
    # Create a new hash object using sha256 which is used by Bitcoin
    hash = hashlib.sha256() 

    # Update the hash object with our user input
    hash.update(user_input.encode('utf-8'))

    # Step 3: Demonstrate the avalanche effect by flipping a single bit
    
    # Convert user_input to binary 
    # Source: https://www.geeksforgeeks.org/python/python-convert-string-to-binary/
    binary_input = ''.join(format(ord(char), '08b') for char in user_input)

    print("\nUnflipped string: ", binary_input)
    
    # Read the first bit then flip it
    first_bit = binary_input[0]

    if first_bit == '0':
        binary_input = '1' + binary_input[1:]
    else:
        binary_input = '0' + binary_input[1:]
    
    print("Flipped string: ", binary_input)

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

    if len(hash_digest) != len(modified_digest):
        print("Error: Hash digests do not have matching length")
        return None

    # Convert both hashes into binary format
    LENGTH = 256

    # Use .digest() method here for accuracy
    binary_hash = ''.join(format(byte, '08b') for byte in hash.digest())
    binary_modified = ''.join(format(byte, '08b') for byte in modified_hash.digest())

    # XOR the hashes to look for differences
    xor_string = ''
    flipped_bits = 0

    for i in range(LENGTH):
        current = str(int(binary_hash[i]) ^ int(binary_modified[i]))
        xor_string += current

        if current == '1':
            flipped_bits += 1

    print("\n---Analysis---")
    avalanche_effect = flipped_bits / LENGTH
    print(f"Avalanche Effect = {avalanche_effect} (Higher is better)")

    # Return hash value and original string length for use in pre-image testing
    return hash.hexdigest(), len(user_input)

target_hash, string_length = question1(user_input)

# Pre-image resistance
print("\n---Pre-image Resistance Tests---")
print("Target Hash:", target_hash)

MAX_ATTEMPTS = 10 # Adjust as needed

guess_hash = hashlib.sha256()

for i in range(MAX_ATTEMPTS):
    # Randomly generate a string of same length and case as user input
    guess = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(string_length))

    print(f"\nAttempt {i + 1}: {guess}")
    
    guess_hash.update(guess.encode('utf-8'))
    guess_digest = guess_hash.hexdigest()
    print(guess_digest)

    if guess_digest == target_hash:
        print("MATCH FOUND!")
        break