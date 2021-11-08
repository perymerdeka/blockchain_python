from hashlib import sha256


class Blockchain:
    def __init__(self, prev_hash: str, transaction_list: list):
        self.prev_hash = prev_hash
        self.transaction_list = transaction_list

        # block data and concate strings
        self.block_data = " - ".join(transaction_list) + " - " + prev_hash
        self.block_hash = sha256(self.block_data.encode()).hexdigest()

    # getting transaction
    def get_transaction(self):
        print(f"block data: {self.block_data}")
        print(f"block hash: {self.block_hash}")

# code exec
if __name__ == "__main__":
    trans1: str = "Anna send 1 BTC to Feri"
    trans2: str = "Feri Send 1.3 BTC to Budi"
    trans3: str = "Bagus Send 3.5 BTC to Hadi"
    trans4: str = 'Ivan send 5.5 BTC to Feryy'

    # transaction List
    transact: list = [trans1, trans2, trans3, trans4]

    # define class and Call Method
    initial_block: Blockchain = Blockchain("Initial String", transact)
    initial_block.get_transaction()

    # the second block
    seconds_block: Blockchain = Blockchain(initial_block.block_hash, [trans2, trans4])
    seconds_block.get_transaction()

    # third block
    third_block = Blockchain(seconds_block.block_hash, [trans1, trans3, trans2])
    third_block.get_transaction()