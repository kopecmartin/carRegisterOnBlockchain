#!/usr/bin/python3.6

from miner import Miner

import ast
from multiprocessing import Process, Manager
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
DIFFICULTY = 2
GENESIS_BLOCK = {
    "hash": "0"
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
                print(data.decode())
                # in python3 the string must be encoded
                conn.sendall("hello from server side".encode())
                # a new block was sent to the blockchain network and is
                # gonna be send to each miner in the network
                miners(ast.literal_eval(data.decode()), blockchain)


def miners(block, blockchain):
    print("w", block)
    # create a shared variable and initialize it
    new_block = Manager().dict()
    new_block["block"] = ""
    new_block["validated"] = False

    # in order to simplify this demo, miners will not communicate over p2p,
    # they will be simulated by independent processes
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
        p.join()

    # check if others validated the block
    if new_block["validated"]:
        # add the block to the blockchain
        blockchain.append(new_block["block"].to_string_add_hash())
        print("blockchain", blockchain)
    else:
        print("The block has been rejected!")




if __name__ == '__main__':
    main()
