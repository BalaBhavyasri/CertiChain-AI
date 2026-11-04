from web3 import Web3
import hashlib

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]

print(web3.is_connected())

contract_address = "0x0F2c756207c7F76AeF69657296ab131B18423B73"
abi = [
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "hash",
        "type": "string"
      }
    ],
    "name": "storeHash",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "hash",
        "type": "string"
      }
    ],
    "name": "verifyHash",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]

contract = web3.eth.contract(
    address=contract_address,
    abi=abi
)

def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def store_hash(hash_value):

    tx_hash = contract.functions.storeHash(
        hash_value
    ).transact()

    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    return receipt

def verify_hash(hash_value):

    return contract.functions.verifyHash(
        hash_value
    ).call()

def detect_tampering(text):

    hash_value = generate_hash(text)

    exists = verify_hash(hash_value)

    if exists:
        return "✅ Original Certificate"

    else:
        return "❌ Tampered Certificate"
    
def authenticity_score(text, skills, info):

    score = 0

    # Blockchain verification
    if detect_tampering(text) == "✅ Original Certificate":
        score += 40

    # Skills detected
    if len(skills) > 0:
        score += 20

    # Important fields found
    important_fields = [
        info.get("Name"),
        info.get("Organization"),
        info.get("Course")
    ]

    filled_fields = sum(
        field is not None and field != "Not Found"
        for field in important_fields
    )

    score += filled_fields * 10

    # OCR text quality
    if len(text) > 50:
        score += 10

    return min(score, 100)

sample_text = "Vaishnavi completed Python course at AICTE"

# Store original certificate hash
hash_value = generate_hash(sample_text)

store_hash(hash_value)

skills = ["Python"]

info = {
    "Name": "Vaishnavi",
    "Organization": "AICTE",
    "Course": "Python"
}

score = authenticity_score(
    sample_text,
    skills,
    info
)

print("Authenticity Score:", score, "%")