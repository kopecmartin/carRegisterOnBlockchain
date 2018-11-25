# carRegisterOnBlockchain

This demo is just a very simple blockchain implementation for presentation
purposes only. It should help the audience to better imagine what blockchain is
and how it works.

## About
We have come up with the idea of car registration based on blockchain, while we
were working on a school project whose aim was to explain technologies like
blockchain and smart contracts and find a real life example where usage of
those technologies would made people's life easier and more secure.

### Why would we want to have something like that?
Buying a car and transferring its ownership is quite expansive process which
takes certain amount of time and often this process is very bureaucratic.

Apart from time and money, when you're buying a used car, you need to
trust the seller that the information he provides are true. The biggest issue
seems to be that the sellers many times lie about the car's mileage.

A car's mileage is difficult to verify, mainly when the car was transferred
from one country to another (take EU as an example) by a car dealer or car
reseller. Usually, the cars dealers change car's mileage to lower in order to
increase attractivity of the car among potential buyers. Governments' systems
are not ideally interconnected with the systems in other EU states and car
resellers took an advantage of it.

In most countries of EU when a car's owner got changed, the new owner needs to
issue a new plate number. This is expansive, time consuming and it's not ideal
for the environment. Also the new owner gets a new technical paper of the car
where all car's information are stated (technical parameters and the owner
information).
That's not a cheap process, too. What is the point of the paper? It's used when
a driver is randomly controlled by a car patrol to identify the car and the
owner.


### What would the system based on blockchain change?
The process of transferring an ownership would become more transparent

#### Advantages:
- trust in the car's history (its mileage, country of origin, ...)
- one plate number for the whole car's life
- no need of having (and issuing) a technical paper of the car - all the
  information would be saved in the blockchain
- owner's time would be saved because visits of the official government
 offices would be reduced to very minimum.

So based on above facts, the car owners would save money, time and would gain
a trust in the car's history. Also it would be better for our environment
thanks to the reduction of paperwork and no need to issue a new plate number
all over again.

#### How would it work?

##### Type of users
We can divide users into two groups:
1. owner of a car
2. others (manufacturers, certified service stations, notary/banks, ...)

Everyone who wants to create a transaction in the blockchain needs to be
provided by a key. It’s a similar process to trading cryptocurrencies.

For a user of type 1, the key is provided by police, which helds all personal
information about the user.

A user of type 2 is a user with a certain business aim (manufacturer,
a service station, ...). That's why these users need to be regulated by a
government department. The department provides them the keys, files their
personal information and runs an official web site where users of type 1 can
easily find and identify users of type 2. Thanks to that, a user of type 1 can
easily verify which dealer or car reseller is the car from.

In order to demotivate users of type 2 to cheat, they are required to stake
a certain amount of money, which they lose if the government department proofs
them guilty of creating a transaction with false information. They wouldn't
lose only the stake but also the permission to run their business.

##### A manufacturer
After a car is manufactured, it's added to the blockchain providing basic
information about the car, it's ID, country of origin, mileage equal to 0 etc.


##### A service station
There are two types of service stations:
1. In EU it's required to visit (every 2 years) a service station regulated by
   government in order to check basic functionality of the car - the station
   needs to decide if the car is able to fully functionate in the traffic
2. The other service stations, which aren't regulated that much, are taking
   care of repairing cars.

Let's say, the service stations of type 1 adds also a mileage check,
which means, they would create a transaction in the blockchain which increases
the mileage of the car. In most EU countries the mileage check is done by
police, only when a car ownership got changed. So if the service station does
mileage checks, the interval between checks is reduced and therefore the
tempering with the mileage is less effective and less attractive.

##### Changing a car ownership
The seller and the buyer create a smart contract, which needs to be validated
by someone. The validation then triggers the smart contract. So the someone
needs to check if the money were transferred which could be done by a notary
or a bank.

##### Government
- police (issuing new keys for users of type 1, registration of users' personal
  data).
- a department for regulating users of type 2


##### Miners
Only the blockchain itself would be public, however, miners will stay private.
The miners are government servers and servers provided by users of type 2. To
motivate these users to provide a server for mining they would pay less fees
for running their business.

Miners are private, so the network should be secured from 51% attack and users
of the network will still have a trust in it, because it is used widely in
EU, so even if a user doesn't trust to government of the country he lives
in, he believes in the date in the blockchain because they were validated by
all countries and all users of type 2 - therefore it's very unlikely to
temper with the data, because it's unlikely that all miners would reach a
consensus to do so.

##### Police check / car patrol
A policeman scans the car plate, finds out the public key of the owner (it's
public information stored in the blockchain) and then will use the public key
to search the owner in the police database (this is a private system, only
police can see this information)




## Demo Implementation
In order to simplify this demo, p2p network and communication among miners
is simulated by multiprocesses.

`blockchain.py` represents the whole network including miners. The network is
implemented as a python server which creates 3 independent processes (miners)
when it receives a new block to validate.

`block.py` contains a Block class that represents a block of blockchain.

`miner.py` contains a Miner class that represents a miner.

# Install
No special installation needed, just `python 3.6` is required

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


# Authors
[Martin Kopec](https://www.linkedin.com/in/martin-kopec-07b29096/)

[Robert Albrecht]()

[Daniel Vitek]()


