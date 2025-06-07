import hashlib
import time

# in this question i have decided to make it a little interactive as we have to give data input of blocks 
# accordingly so that we can see change of hash ( before and after ) and learn dynamically.
# here we have full control on what block data we could change and we can observe the change 
# of hash as well ,where needed
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

    def updateHash(self):
        self.timestamp = time.time()  # latest timestamp
        self.hash = self.calculateHash()

    def __str__(self):
        return (
            f"Block {self.index}:\n"
            f"  Data: {self.data}\n"
            f"  Previous Hash: {self.previousHash}\n"
            f"  Hash: {self.hash}\n"
            
        )
# instead of changing and checking the data/hash change in just 1 block , i implemented it this way
# so that we can change any block data we want . also i initialized it this way that we give data input
# to all 3 blocks and we can change whatever we want thru this setup.
print("Enter data for blocks 0, 1, and 2:")
data0 = input("Data for Block 0: ")
data1 = input("Data for Block 1: ")
data2 = input("Data for Block 2: ")

block0 = Block(0, data0, "0")
block1 = Block(1, data1, block0.hash)
block2 = Block(2, data2, block1.hash)

blockchain = [block0, block1, block2]

def displayChain(chain):
    for block in chain:
        print(block)

print("\nOriginal Blockchain:")
displayChain(blockchain)

tamper_block_num = input("\nWhich block to tamper? (0/1/2): ")

if tamper_block_num not in ["0","1","2"]:
    print("Invalid block number!")
    exit()

tamper_block_num = int(tamper_block_num)

print(f"Current data in Block {tamper_block_num}: {blockchain[tamper_block_num].data}")
new_data = input("Enter new data for tampering: ")

blockchain[tamper_block_num].data = new_data
blockchain[tamper_block_num].updateHash()

for i in range(tamper_block_num + 1, len(blockchain)):
    blockchain[i].previousHash = blockchain[i-1].hash
    blockchain[i].updateHash()

print("\n🔔 Tampering detected! Hashes updated accordingly.\n") 

print("Updated Blockchain:")
displayChain(blockchain)
