import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Blockchain RPC URLs & API Keys
ETH_INFURA_RPC_URL = os.getenv("ETH_INFURA_RPC_URL")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

# Ensure required environment variables are loaded
REQUIRED_ENV_VARS = ["ETH_INFURA_RPC_URL", "ETHERSCAN_API_KEY"]
missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Web3 Instance
WEB3_INSTANCE = Web3(Web3.HTTPProvider(ETH_INFURA_RPC_URL))

# Etherscan API Config
ETHERSCAN_API_URL = "https://api.etherscan.io/api"
ETHERSCAN_GET_ABI_ENDPOINT = (
    f"{ETHERSCAN_API_URL}?module=contract&action=getabi&address={{address}}&apikey={ETHERSCAN_API_KEY}"
)
