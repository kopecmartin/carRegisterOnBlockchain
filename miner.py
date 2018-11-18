#!/usr/bin/python3.6

from block import Block


class Miner:
    def __init__(self, id, block, blockchain, difficulty, new_block):
        self.id = id
        self.block = block
        self.blockchain = blockchain
        self.difficulty = difficulty
        self.new_block = new_block

    def is_blockchain_valid(self):
        pass

    def is_block_valid(self):
        pass

    def _get_previous_hash(self):
        return self.blockchain[-1]['hash']

    def mine(self):
        new_block = Block(self.block['timestamp'], self.block['data'])
        # link the block to the previous block
        new_block.previous_hash = self._get_previous_hash()
        #while
        # get hash
        new_hash = new_block.get_hash()
        # check hash rules
        print(new_hash)
        new_block.hash = new_hash
        # increase nonce
        #new_block.increment_nonce()
        if self.new_block["block"] == "":
            # this process has found the hash first
            self.new_block["block"] = new_block
            print(self.id, " mined the block")
        else:
            # validate the block found by other process (miner)
            print("The hash has been already found, let's validate it.")

            print("validating")
            self.new_block["validated"] = True
