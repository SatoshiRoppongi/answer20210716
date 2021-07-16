# -*- coding: utf-8 -*-

"""
    calc_merkle_root.py

"""
import hashlib

# double sha256
# https://en.bitcoin.it/wiki/Protocol_documentation#Merkle_Trees
def dhash(a):
    """
    calculates a's double sha256
    """
    return hashlib.sha256(hashlib.sha256(a.encode()).hexdigest().encode()).hexdigest()

def convert_endian(hash):
    # https://qiita.com/QUANON/items/e3d91a6f33536bd0de5a
    hex_be = hash
    bytes_be = bytes.fromhex(hex_be)
    bytes_le = bytes_be[::-1]
    hex_le = bytes_le.hex()
    return hex_le

def make_hash(hash_array):
    """
    Recursive functkion that dirives Merkle root.
    """

    if len(hash_array) == 1:
        return hash_array[0]

    if len(hash_array) % 2 == 1:
        # When number of array is an odd, duplicate the last element and append to last.
        # It is assumed to be executed one time.
        hash_array.append(hash_array[-1])

    parent_node = []
    while len(hash_array) != 0:
        left_child = dhash(convert_endian(hash_array.pop(0)))
        right_child = dhash(convert_endian(hash_array.pop(0)))
        new_hash = convert_endian(dhash(left_child + right_child))
        parent_node.append(new_hash)

    return make_hash(parent_node)

def main():
    tx_hashes= ['d440c2e3e0a708ce82c1b8e01155f9f350b41b97020d754a77bc0621730ac2e5', 
                '9842893448d6f7534f5f82737094804c4fe9ec551de0fc6844d945f4736db3e8', 
                'fdacd62551099230552d776d1d92cff1a928172ea6e4970c976be939287e86ec', 
                'af762cf30b5a536601f5159852de776d73942bf48e1d5adaf91937b3d8f773f3', 
                'a4d26e4e35f0c821c9e71286fdcf4566f3bfc77dcd092684ab21ef34becb78f9', 
                '828f1be2e3896a62c7a1ae1b5033a6f8540002d3b06b889181ec0e35612b3315', 
                '0456df2b357f041d414211f10ed3e5b8dbf29141bd9de9c9594b97f843c9ae6c', 
                'ca3789839b6e838343b089c6d206ccbfd5b1caa611453297b130cfb835e2dccb', 
                '9255a032a8b52f4ab23a349344a601f016b8997a3b8a533c8a64779f66b759ac' 
                ]
    merkle_root = make_hash(tx_hashes)
    print(merkle_root)

if __name__ == "__main__":
    main()    


