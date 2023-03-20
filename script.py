from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

new_transactions1 = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

my_blockchain = Blockchain()
print(my_blockchain.add_block(new_transactions))
print(my_blockchain.add_block(new_transactions1))
# my_blockchain.print_blocks()

modified_block = my_blockchain.chain[2]
modified_block.transactions = [
    {'amount': '-999999', 'sender':'alice', 'receiver':'bob'},
    {'amount': '55', 'sender':'bob', 'receiver':'alice'}
]
my_blockchain.validate_block_chain()