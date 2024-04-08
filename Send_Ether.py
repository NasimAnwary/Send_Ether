
# Import required libraries
from web3 import Web3
import json

# Connect to an goerli testnet node using an infura link
Goerli_url = 'https://goerli.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'
web3_connect = Web3(Web3.HTTPProvider(Goerli_url))

# Specify account details, private key required for the account from which the ether is being sent
account_from = "0xD31Ea25d8d5Eee53E8FD0b54140aA4c9"
account_to = "0x3b6b3Aa1cE0967f044b11A3Cf214e5f08"
private_key = ""

# Obtain the nonce of the transaction account. This is required in the transaction 
nonce = web3_connect.eth.get_transaction_count(account_from)

# Build the transaction
tx = {
    'nonce': nonce,
    'to': account_to,
    'value': web3_connect.to_wei(0.0005, 'ether'),
    'gas': 200000,
    'gasPrice': web3_connect.to_wei(1, 'gwei')
}

# Sign the transaction with the private key. This creates a valid transaction 
signed_tx = web3_connect.eth.account.sign_transaction(tx, private_key)

# Send the transaction to the ethereum network and return the transaction hash
tx_hash = web3_connect.eth.send_raw_transaction(signed_tx.rawTransaction)

# You can use the transaction hash to find the transaction on Etherscan
print(tx_hash)

