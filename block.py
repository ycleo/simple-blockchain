import datetime
from hashlib import sha256

# Block: time stamp, previous hash, transaction data -> generate hash
class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()
    
    def print_contents(self):
        print("- timestamp:", self.time_stamp)
        print("- transactions:", self.transactions)
        print("- current hash:", self.generate_hash())
        print("- previous hash:", self.previous_hash, "\n") 

# transaction1 = {
#   'amount': '30',
#   'sender': 'Alice',
#   'receiver': 'Bob'
# }

# transaction2 = {
#   'amount': '20',
#   'sender': 'Alex',
#   'receiver': 'Bob'
# }

# transactions = [transaction1, transaction2]

# b = Block(transactions, 0)
# b.print_contents()