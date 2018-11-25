#!/usr/bin/python3.6

import hashlib


class Block:
    def __init__(self, timestamp, car, id):
        self.timestamp = timestamp
        self.car = car
        self.id = id
        # the following is up to a miner
        self.nonce = 0
        self.previous_hash = ""
        self.hash = ""

    def increment_nonce(self, number):
        self.nonce += number

    def get_block_obj(self, add_hash=False):
        """Returns the block as a dictionary.

        :param add_hash: Whether hash of the block is included or not
        :type add_hash: Bool
        :rtype: dict
        """
        ret = {
            "timestamp": str(self.timestamp),
            "car": str(self.car),
            "id": str(self.id),
            "previous_hash": self.previous_hash,
            "nonce": str(self.nonce)
        }
        if add_hash:
            ret.update({"hash": self.hash})
        return ret

    def to_string(self):
        """Returns the block object (dict) in a string format.

        :rtype: string
        """
        return str(self.get_block_obj())

    def to_string_add_hash(self):
        """Returns the block object (dict) including
        its hash in a string format.

        :rtype: string
        """
        b = self.get_block_obj()
        b["hash"] = self.hash
        return str(b)

    def get_hash(self):
        """Calculates a hash of the block.

        :return: a hash of the block
        :rtype: string
        """
        return hashlib.sha224(self.to_string().encode()).hexdigest()

    def is_block_valid(self):
        """Checks block's validity.

        A block is valid if: TODO

        :return: True if the block is valid, otherwise False
        :rtype: Bool
        """
        # first check if the hash was calculated correctly
        if self.hash != self.get_hash():
            return False
        # check integrity and validity of the data
        # TODO

        return True
