#!/usr/bin/python3.6

from block import Block


class Miner:
    """The class represents a miner and implements methods
    related to the role
    """

    def __init__(self, id, block, blockchain, difficulty, new_block):
        self.id = id
        self.block = block
        self.blockchain = blockchain
        self.difficulty = difficulty
        self.new_block = new_block

    def is_blockchain_valid(self, last_block=[]):
        """Checks blockchain's validity.

        The blockchain (in our case) is valid if every block contains
        the hash of the previous one.

        :param last_block: if defined, the blockchain's validity is checked
        with that block included
        :type last_block: block object
        """
        if last_block:
            last_block = [last_block.get_block_obj(True)]
        if len(self.blockchain) == 0:
            return False
        i = 0
        for block in self.blockchain + last_block:
            if block["hash"] == "0":
                # the first block
                continue
            if self.blockchain[i]["hash"] != block["previous_hash"]:
                return False
            i += 1
        return True

    def _get_previous_hash(self):
        """Returns a hash of the last block in the blockchain.

        :return: hash of the last block in the blockchain
        :rtype: string
        """
        return self.blockchain[-1]['hash']

    def mine(self):
        """Calculates a hash of a block and validates the whole block then."""
        new_block = Block(self.block['timestamp'], self.block['car'],
                          self.block['id'])
        # link the block to the previous block
        new_block.previous_hash = self._get_previous_hash()
        while True:
            # get a hash
            new_hash = new_block.get_hash()
            # check hash rules, in our case check if the hash starts with
            # self.difficulty number of zeroes
            if new_hash[0] != self.difficulty * "0":
                if self.new_block["block"] is None:
                    # the hash hasn't been found yet by any other process,
                    # therefore increase the nonce and continue
                    # miners will use a different mining mechanism in order
                    # to increase the probability of finding a hash by
                    # a different miner
                    new_block.increment_nonce(self.id + 1)
                    continue
                break
            break

        # NOTE: May happen that two processes find the hash at the same time,
        # because there is not a big difficulty, however, it's not a problem,
        # for sake of the demo it's fine

        if self.new_block["block"] is None:
            # this process has found the hash first
            print(self.id, " - the winner hash", new_hash)
            new_block.hash = new_hash
            self.new_block["block"] = new_block
            print(self.id, " - mined the block")
        else:
            # validate the block found by other process (miner)
            if self.new_block["validated"] is not False:
                print(self.id, " - validating")
                # check block's validity
                valid = False
                if self.new_block["block"].is_block_valid():
                    # check blockchain's validity when we apply the newly
                    # mined block
                    if self.is_blockchain_valid(self.new_block["block"]):
                        valid = True
                self.new_block["validated"] = valid
            else:
                # NOTE: this demo doesn't take into account the number of
                # miners who approved the block, the block will be rejected
                # if any of them rejected it
                # but usually just more than 50% of miners must approve
                print(self.id, " - the block has been rejected by other miner")
