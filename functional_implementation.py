from hashlib import sha256


# linking func
def linked_data(prev_hash: str, transaction_list: list):
    block_data: str = " - ".join(transaction_list) + prev_hash
    block_hash: str = sha256(block_data.encode()).hexdigest()
    return block_data, block_hash

if __name__=='__main__':
    trans1: str = "Anna send 1 BTC to Feri"
    trans2: str = "Feri Send 2.3 BTC to Budi"
    trans3: str = "Bagus Send 3.4 BTC to Hadi"
    trans4: str = 'Ivan send 5.5 BTC to Feryy'

    # transaction List
    transact: list = [trans1, trans2, trans3]

    # call func
    linked = linked_data('Initial String', transact)
    # get value
    print(linked)