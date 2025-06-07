# in this question i have decided to make it a little interactive as we have to give data input of block 
# accordingly so that we can see change of hash and nonce dynamically 
import hashlib
import time
# created block as before, basic
class Block:
    def __init__(self, index, data, previousHash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previousHash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mineBlock(self, difficulty):
        prefix_str = '0' * difficulty # diff means no of zeros to be wanting or say a particular
        # situation/demand being fulfilled. just like for loop for recursion
        # in recursion, loops keep executing till it meets rew for 'for' loop or terminated
        # nonce is also like that , creating hash till the diff, demand/req are met, now that no
        # times it is taking hash to be fulfilled is nonce.
        # nonce is basically count for being req satisfied
        print(f"\nMining block {self.index} of difficulty {difficulty} (should start with '{prefix_str}')")
        start = time.time()
        attempts = 0

        while not self.hash.startswith(prefix_str):
            self.nonce += 1
            self.hash = self.calculateHash()
            attempts += 1 # kinda nonce count
        
        end = time.time()
        print(f"Block {self.index} mined")
        print(f"  Nonce found: {self.nonce}")
        print(f"  Attempts or Counts: {attempts}") 
        print(f"  Time taken: {end - start:.4f} seconds")

    def __str__(self):
        return (
            f"Block {self.index}:\n"
            f"  Data: {self.data}\n"
            f"  Previous Hash: {self.previousHash}\n"
            f"  Nonce: {self.nonce}\n"
            f"  Hash: {self.hash}\n"
            
        )

print("Enter data for blocks 0, 1, and 2:")
data0 = input("Data for Block 0: ")
data1 = input("Data for Block 1: ")
data2 = input("Data for Block 2: ")

block0 = Block(0, data0, "0")
difficulty = 4  # number of leading zeros required in hash, to be fulfilled
prefix_str = '0' * difficulty
tick = '\u2714'  # code for ✔, so that it shows that goal/aim is completed and defined in
# the output terminal

print(f"\nStarting mining with difficulty = {difficulty} zeros ({prefix_str})  {tick}")

block0.mineBlock(difficulty)

# using blocks hash for prev hash matching
block1 = Block(1, data1, block0.hash)
block1.mineBlock(difficulty)

block2 = Block(2, data2, block1.hash)
block2.mineBlock(difficulty)

blockchain = [block0, block1, block2]

print("\nBlockchain after mining:")
for block in blockchain:
    print(block)
