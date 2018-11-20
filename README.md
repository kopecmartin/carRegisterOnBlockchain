# carRegisterOnBlockchain

## About
TODO


## Implementation
In order to simplify this demo, p2p network and communication among miners
is simulated by multiprocesses.

`blockchain.py` represents the whole network including miners. The network is
implemented as a python server which creates 3 independent processes (miners)
when it receives a new block to validate.

`block.py` contains a Block class that represents a block of blockchain.

`miner.py` contains a Miner class that represents a miner.

# Install
No special installation needed, just python 3.6 is required

# Run
Start the network and initialize blockchain by:
```
$ ./blockchain.py
```
In a second terminal execute the following:
```
$ ./transaction.py
```
in order to create a block which will be mined by miners (processes).

# Run Scenarios
TODO transaction types



