import hashlib
import string
import time
import random

class Block:
    def __init__(self, id, timestamp, data, previous_hash, nonce, hash):
        self.id = id
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = hash

    # Asked ChatGPT to make this look like a block
    def __str__(self):
        lines = [
            f"│ Block ID    : {self.id}",
            f"│ Timestamp   : {self.timestamp}",
            f"│ Data        : {self.data}",
            f"│ Nonce       : {self.nonce}",
            f"│ Hash        : {self.hash}",
            f"│ Prev. Hash  : {self.previous_hash}",
        ]
        width = max(len(line) for line in lines)
        top = "┌" + "─" * (width - 2) + "┐"
        bottom = "└" + "─" * (width - 2) + "┘"
        return "\n".join([top] + lines + [bottom])

# Get the current block's hash based on the previous + the current data
def set_hash(previous_hash, data):
    hashObject = hashlib.sha256()
    hash_string = f"{previous_hash} + {data}"
    hashObject.update(hash_string.encode('utf-8'))
    return hashObject.hexdigest()

# Generate dummy data
data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# Create the first block
genesis_block = Block(
    id=0,
    timestamp=time.time(),
    data=data,
    previous_hash="000",
    nonce=0,
    hash = set_hash(previous_hash="000", data=data)
)

# Display the first block
print(genesis_block)

# Store all blocks
blockchain = []
blockchain.append(genesis_block)

# Delay the creation of new blocks with computational proof-of-work system
    # Github Copilot
def mine_block_space(previous_hash, data, difficulty=5):
    start = time.time()
    print("\nMining a new block...")
    nonce = 0
    target = "0" * difficulty
    while True:
        hash_attempt = set_hash(previous_hash, f"{data}{nonce}")
        if hash_attempt.startswith(target):
            end = time.time()
            print(f"Block found in {end - start}")
            return nonce, hash_attempt
        nonce += 1

# Create subsequent blocks
def create_block(previous_block, data):
    nonce, block_hash = mine_block_space(previous_block.previous_hash, previous_block.data)
    new_block = Block(
        id=previous_block.id + 1,
        timestamp=time.time(),
        data=data,
        previous_hash=previous_block.hash,
        nonce=nonce,
        hash=block_hash
    )

    blockchain.append(new_block)
    print(new_block)

# Example transactions
for i in range(5):
    data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    new_block = create_block(blockchain[-1], data)