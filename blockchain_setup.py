from web3 import Web3

# Sambungan ke Ethereum node (gunakan Infura atau Ganache)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Semak sambungan
if w3.isConnected():
    print("Berjaya disambung ke Ethereum Network!")
else:
    print("Sambungan gagal.")

# Menyiapkan alamat kontrak pintar
contract_address = "0xYourContractAddress"
contract_abi = [...]  # ABI kontrak pintar

# Berhubung dengan kontrak pintar
contract = w3.eth.contract(address=contract_address, abi=contract_abi)
