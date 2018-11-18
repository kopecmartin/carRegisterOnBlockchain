# carRegisterOnBlockchain

## About



## Implementation
In order to simplify this demo, p2p network and communication among miners
is simulated by multiprocesses.

`blockchain.py` represents the whole network including miners. The network is
implemented as a python server which creates 3 independent processes (miners)
when it receives a new block to validate.

`block.py` contains a Block class that represents a block of blockchain.

`miner.py` contains a Miner class that represents a miner.

# Install

```
$ virtualenv .venv
$ source .venv/bin/activate
(.venv)$ pip install -r requirements.txt
```


# Run



# Run Scenarios




