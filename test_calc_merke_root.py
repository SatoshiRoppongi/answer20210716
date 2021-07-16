# -*- coding: utf-8 -*-

"""
    calc_merkle_root.py

"""
import requests
import calc_merkle_root

base_url = "https://blockchain.info/rawblock/"
block_hash = "000000000000000000042cef688cf40b4a70ac814e4222e6646bd6bb79d18168"
request_url = base_url + block_hash

ret = requests.get(request_url)
transactions = list(map(lambda tx: tx["hash"], ret.json()["tx"]))

print(len(transactions))
merkle_root = calc_merkle_root.make_hash(transactions)
print(merkle_root)
