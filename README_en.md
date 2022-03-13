## Open Seed
[ZH](/README.md)  [EN](/README_en.md)

Open Seed is a smart contract that provides random seeds to researchers and guarantees the authenticity of the random process.

**👨🏻‍💻 You can access [Ropsten testnet](https://ropsten.etherscan.io/address/0xe618A5DCA9cda2f43696641D670936851Ac58D15) to use Open Seed.**

## Motivation
Researchers often claim in their papers:

- We randomly selected several samples. (``Random sampling``)
- We randomly ordered samples. (``Random sorting``)
- We set a random initial value. (``Random value``)
- etc.

### How to prove that the random process is real?

Someone may choose a particular value, i.e., the date of a holiday or anniversary, to prove that they are not manipulating the random process. However, there are many such values, so a dishonest one can try many times to find a random seed that works in their favor.
Therefore,
**a random seed must be associated with a purpose.**

After obtaining a random seed, a dishonest one may change the sample set or data to make the random result in his favor.
For example, he might exclude some unfavorable samples, or construct a biased sequence. Therefore,
**once the random seed is revealed, the sample set cannot be modified.**

In addition, **the random source should be credible and unbiased.**

### **Random Source Server**
- Users can submit an application to the server, and the server will return a random seed to him.
- An application needs to explain the hash value of the sample set and the purpose of the random seed.
- All application records are public, and everyone can query the server for one's record.

>✔️ The public records ensure that a user cannot test multiple random seeds (to find a biased one) for an experiment, and the hash value ensures that data cannot be arbitrarily changed.

>🌐 Of course, a user should disclose his data and the random procedure.

### **Smart Contract**
A blockchain is essentially a distributed ledger, and the hash values of blocks are good random seeds [[On Bitcoin as a public randomness source](https://eprint.iacr.org/2015/1015)].
We have implemented a decentralized random source through smart contracts, and everyone can get a random seed by calling a smart contract.

>⚠️<b>Warning:</b> You cannot use on-chain data such as ``blockhash``, `block.timestamp` as random seeds for smart contracts because miners can manipulate them.


## Quick Start
>👉 If you are a newbie, please read [How to run a smart contract](#How-to-run-a-smart-contract) first.

> ⚙️ Open Seed contract deployed on [Ethereum Ropsten testnet](https://ropsten.etherscan.io).\
🔗 Contract Address: [0xe618A5DCA9cda2f43696641D670936851Ac58D15](https://ropsten.etherscan.io/address/0xe618A5DCA9cda2f43696641D670936851Ac58D15)

Open Seed uses struct ``Record`` to record the status of each random seed.

**Step 1: Create a record**

We use the function ``create`` to create a seed record.
There are three arguments in the function ``create``:
+ ``_desc``: Purpose of using the random seed
+ ``_data_sha256``: SHA-256 of the data
+ ``_data_ipfs``: URL or IPFS of the data

>🔔 On-chain storage is expensive, Open Seed uses ``bytes32`` to store data on the blockchain, so the data lengths is limited to 32 bytes (or 64 chars).
Please store the SHA-256 and provide data elsewhere if you want to store more data.

📌 You can use [bytes32Utils.py](/openseed/bytes32Utils.py) to convert *string* and *bytes32*.

After the miner confirms the transaction *create*, we can view log ``_stateChange(address, record_id, state)`` to get ``record_id`` (the id of record). We use ``record_id`` to update or query this record in the following.

Read function ``getUserRecords`` shows the user's all seed records.

**Step 2: Get the random seed**

In the next block, we call the function ``update`` to refresh the random seed in the record.
We can view log ``_openSeed(address, record_id, random seed)`` to get *random seed*.

```python
#The random seed is a block's hash value (bytes32).
import random
random.seed(0x79baf4f5dd317ed2916d6854ef3deaf8e7e1d04f32a6094a06c91f52213ddcd1)
print(random.random())
```

**Step 3: Lock the record**

We should provide ``smart contract address``, ``wallet address`` and ``record_id`` in the paper, so everyone can check the authenticity of our experiment.
- ``getOneRecord(wallet address, record_id)``
- ``getUserRecords(wallet address)``

After the paper is published, we call the function ``lock`` to associate our work with this record and lock this record.


>🔔 A researcher should always use the same wallet address to create random seed.\
>🔔 A paper/research should be associated with only one seed record. If you need more random seeds, you can use this random seed to generate.


## How to run a smart contract

- Ethereum Wallet
    - [MetaMask Tutorial for Beginners - How to Set Up MetaMask](https://www.youtube.com/watch?v=Af_lQ1zUnoM)
    - [Metamask Install](https://metamask.io/)
- Ropsten testnet faucet
    - [How to Get Test Ether From Faucet on Ropsten Network](https://www.youtube.com/watch?v=rSL3kP13gOI)
    - https://ropsten.oregonctf.org/
    - https://faucet.egorfine.com/
    - https://faucet.metamask.io/
- Etherscan - [How To Use and Read Etherscan In 10 Minutes](https://youtu.be/DKBQ63txuZI?t=475)
- IPFS (free 1GB of storage) -  https://www.pinata.cloud/

## Citation
```
 @article{open_seed, 
          title={Open Seed}, 
          url={https://github.com/d0scoo1/OpenSeed}, 
          author={Kailun Yan}} 
 ```

## License
MIT: https://github.com/d0scoo1/OpenSeed/blob/main/LICENSE