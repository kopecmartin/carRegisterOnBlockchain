#!/usr/bin/python3.6

from miner import Miner

import ast
from multiprocessing import Process, Manager
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
DIFFICULTY = 1      # Number of zeroes at the beginning of a new hash
GENESIS_BLOCK = {
    "hash": "0",
    "data": "this is the genesis block"
}


def main():
    # initialize blockchain by adding the genesis block
    # and create a file where all blocks will be appended
    blockchain = [
        GENESIS_BLOCK
    ]

    # create a server which simulates all blockchain miners
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(2048)
                print("A new block received: ", data.decode())
                # in python3 the string must be encoded
                conn.sendall("hello from server side".encode())
                # a new block was sent to the blockchain network and is
                # gonna be send to each miner in the network
                miners(ast.literal_eval(data.decode()), blockchain)


def miners(block, blockchain):
    """Creates miners as independent processes and if a new block is
    validated it's added to the blockchain.

    :type block: dict
    :type blockchain: list
    """
    # create a shared variable and initialize it
    # the var is used for communication between processes (miners), when one
    # of them finds the hash of a block, the others will validate the block
    new_block = Manager().dict()
    new_block["block"] = None
    new_block["validated"] = None

    # in order to simplify this demo, miners will not communicate over p2p,
    # network but they will be simulated by independent processes
    # let's create 3 miners which will compete in finding a hash
    miners_lst = []
    for i in range(3):
        miners_lst.append(Miner(i, block, blockchain, DIFFICULTY, new_block))

    # run each miner independently
    jobs = []
    for miner in miners_lst:
        p = Process(target=miner.mine)
        jobs.append(p)
        p.start()

    # join processes
    for p in jobs:
        # NOTE: the processes will be joined here, which means processes which
        # got earlier to this point will wait for the rest of them
        # ^^ above said, we'll wait until all processes validate the block,
        # if any of them rejects it, the block will not be put into the
        # blockchain in the next step
        p.join()

    # check if others have validated the block
    if new_block["validated"]:
        # add the block to the blockchain
        blockchain.append(new_block["block"].get_block_obj(True))
        # TODO nice print so that it's more readable during presentation
        #print("blockchain", blockchain)
        print("BLOCKCHAIN CONTENT")
        for block in blockchain:
            print(block)
    else:
        print("The block has been rejected!")


if __name__ == '__main__':
    main()
