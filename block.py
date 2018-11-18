#!/usr/bin/python3.6

import hashlib


class Block:
    def __init__(self, timestamp, data):
        self.timestamp = timestamp
        self.data = data
        # the following is up to a miner
        self.nonce = 0
        self.previous_hash = ""
        self.hash = ""

    def increment_nonce(self):
        self.nonce += 1

    def get_block_obj(self):
        return {
            "timestamp": str(self.timestamp),
            "data": str(self.data),
            "previous_hash": self.previous_hash,
            "nonce": str(self.nonce)
        }

    def to_string(self):
        return str(self.get_block_obj())

    def to_string_add_hash(self):
        b = self.get_block_obj()
        b["hash"] = self.hash
        return str(b)

    def get_hash(self):
        print("my hash", self.to_string())
        return hashlib.sha224(self.to_string().encode()).hexdigest()

    def is_block_valid(self):
        pass

