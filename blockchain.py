from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_dummy_block()
    
    def create_dummy_block(self):
        dummy_block = Block([], 0)
        self.chain.append(dummy_block)

    def print_all_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()
        
    def add_block(self, transactions):
        previous_hash = self.chain[-1].hash
        new_block = Block(transactions, previous_hash)
        # perform proof of work: "slows down" the process of tampering blocks and also to confirm valid blocks
        proof = self.proof_of_work(new_block, 5)
        self.chain.append(new_block)
        return proof, new_block

    def proof_of_work(self, block, difficulty):
        proof = block.generate_hash()
        while proof[:difficulty] != "0" * difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
    
    def validate_block_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.previous_hash != previous.generate_hash():
                print("The previous block's hash does not equal the previous hash value stored in the current block.")
                return False
            if current.hash != current.generate_hash():
                print("The current hash of the block does not equal the generated hash of the block.")
                return False
        return True