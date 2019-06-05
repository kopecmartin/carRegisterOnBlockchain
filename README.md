# carRegisterOnBlockchain

This demo is just a very simple blockchain implementation for presentation
purposes only. It should help the audience to better imagine what blockchain is
and how it works.

## About
We have come up with the idea of car registration based on blockchain, while we
were working on a school project whose aim was to explain technologies like
blockchain and smart contracts and find a real life example where usage of
those technologies would make people's life easier and more secure.

The full paper is available only in Czech and Slovak language, however, the
practical usage of the technologies we've come up with is described in this
Readme in English.

### Why would we want to have something like that?
Buying a car and transferring its ownership is quite expensive process which
takes certain amount of time and it's often very bureaucratic.

Apart from time and money, when you're buying a used car, you need to
trust the seller that the information he provides is true. The biggest issue
seems to be that the sellers many times lie about the car's mileage.

A car's mileage is difficult to verify, mainly when the car was transferred
from one country to another (take EU as an example) by a car dealer or car
reseller. Usually, the cars dealers decrease car's mileage in order to
increase attractivity of the car among potential buyers. Governments' systems
are not ideally interconnected with the systems in other EU states and cars
resellers have taken an advantage of it.

In most EU countries when a car's owner gets changed, the new owner needs to
issue a new plate number. This is expansive, time consuming and it's not ideal
for the environment. Also the new owner gets a new technical paper of the car
where all car's information are stated (technical parameters and the owner
information).
That's not a cheap process, too. What is the point of the paper? It's used when
a driver is randomly controlled by a car patrol to identify the car and the
owner.


### What would the system based on blockchain change?
The process of transferring an ownership would become more transparent.

#### Advantages:
- trust in the car's history (its mileage, country of origin, ...)
- one plate number for the entire car's life
- no need of having (and issuing) a technical paper of the car - all the
  information would be saved in the blockchain
- owner's time would be saved because visits of the official government
 offices would be reduced to very minimum.

So based on above facts, the car owners would save money, time and would gain
a trust in the car's history. Also it would be better for our environment
thanks to the reduction of paperwork and no need to issue a new plate number
all over again.

### How would it work?

#### Type of users
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
a certain amount of money, which they'll lose if the government department
proofs them guilty of creating a transaction with false information. They
wouldn't loose only the stake but also the permission to run their business.

#### A manufacturer
After a car is manufactured, it's added to the blockchain providing basic
information about the car, it's ID, country of origin, mileage equal to 0 etc.


#### A service station
There are two types of service stations:
1. In EU it's required to visit (every 2 years) a service station regulated by
   government in order to check basic functionality of the car - the station
   needs to decide if the car is able to fully functionate in the traffic
2. The other service stations, which aren't regulated that much, are taking
   care of repairing cars.

Let's say, the service stations of type 1 adds also a mileage check,
which means, they would create a transaction in the blockchain which increases
the mileage of the car. In most EU countries the mileage check is done by
police, only when a car ownership gets changed. So if the service station does
mileage checks, the interval between checks is reduced and therefore the
tempering with the mileage is less effective and less attractive.

#### Changing a car ownership
The seller and the buyer create a smart contract, which needs to be validated
by someone. The validation then triggers the smart contract. So the someone
needs to check if the money were transferred which could be done by a notary
or a bank.

#### Government
- police (issuing new keys for users of type 1, registration of users' personal
  data).
- a department for regulating users of type 2


#### Miners
Only the blockchain itself would be public, however, miners would stay private.
The miners are government servers and servers provided by users of type 2. To
motivate these users to provide a server for mining they would pay less fees
for running their business.

Miners are private, so the network should be secured from 51% attack and users
of the network will still have a trust in it, because it is used widely in
EU, so even if users don't trust the government of the country they live
in, they believe in the data in the blockchain because it was validated by
all countries and all users of type 2 - therefore it's very unlikely to
temper with the data, because it's unlikely that all miners would reach a
consensus to do so.

#### Police check / car patrol
A policeman scans the car plate, finds out the public key of the owner (it's
public information stored in the blockchain) and then will use the public key
to search the owner in the police database (this is a private system, only
police can access it)


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

# Run the demo
Start the network and initialize blockchain by:
```console
$ ./blockchain.py
```
In a second terminal execute the following:
```console
$ ./manufacturer.py
```
in order to create a block which will be mined by miners (processes).
The above script simulates a manufacturer. It generates a random ID which
is considered as an ID of the manufactured car. It sets its mileage to 0 and
sets additional data like manufacturer (Volkswagen), model (Golf), year
(current year), country_of_origin (Czech Republic).

Run the following script to simulate a change of the car ownership.
NOTE: this is a simple demo, so the users doesn't have to exist, you can
make up buyer id, however, as a car id use the one, `manufacturer.py` script
generated in the step above and as a seller id use the manufacturer's id.
```console
$ ./seller.py <seller_ID> <buyer_ID> <car_ID>
```

Run the following script in order to simulate a check when a car's mileage will
be edited.
```console
$ ./service_station.py <car_ID>
```

Try to change the ownership again.
```console
$ ./seller.py <seller_ID> <buyer_ID> <car_ID>
```

Run the following script to list the history of the car. It will print all
blocks where the car_ID is found.
```console
$ ./car_history.py <car_ID>
```


# Authors
[Martin Kopec](https://www.linkedin.com/in/martin-kopec-07b29096/)

[Robert Albrecht](https://www.linkedin.com/in/robert-albrecht498/)

[Daniel Vitek](https://www.linkedin.com/in/daniel-v%C3%ADtek-683399147/)


