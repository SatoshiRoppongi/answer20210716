# -*- coding: utf-8 -*-

import requests
import calc_merkle_root

base_url = "https://blockchain.info/rawblock/"
block_hash = "000000000000000000042cef688cf40b4a70ac814e4222e6646bd6bb79d18168"
request_url = base_url + block_hash

ret = requests.get(request_url)
transactions = list(map(lambda tx: tx["hash"], ret.json()["tx"]))

merkle_root = calc_merkle_root.make_hash(transactions)
print(merkle_root) # 67a637b1c49d95165b3dd3177033adbbbc880f6da3620498d451ee0976d7b1f4
