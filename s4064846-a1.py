import hashlib

# Step 1: Take an arbitrary string as input from the user.
user_input = input("Enter a string: ")

# Step 2: Computes and displays its hash.

# Create a new hash object using sha256 which is used by Bitcoin
hash = hashlib.sha256()

# Update the hash object with our user input
hash.update(user_input)

# Display the hash in hex format
print(hash.hexdigest())

# Step 3: Demonstrate the avalanche effect
