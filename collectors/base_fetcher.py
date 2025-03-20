import os
import json
import requests
import web3
from config.logger import get_logger
from config.onchain_infra import WEB3_INSTANCE, ETHERSCAN_GET_ABI_ENDPOINT

logger = get_logger()

class BaseFetcher:
    """
    A base class for fetching on-chain data from DeFi protocols.
    Handles Web3 interactions, ABI fetching, and contract instantiation.
    """

    def __init__(self) -> None:
        """Initialize with a Web3 instance."""
        self.web3_instance = WEB3_INSTANCE

    def get_contract(self, contract_address: str, abi: list) -> web3.eth.Contract:
        """
        Returns a Web3 contract instance.

        Args:
            contract_address (str): The smart contract address.
            abi (list): The ABI of the contract.

        Returns:
            Web3.eth.Contract: The Web3 contract instance.
        """
        return self.web3_instance.eth.contract(address=contract_address, abi=abi)

    def fetch_abi_from_etherscan(self, contract_address: str) -> list:
        """
        Fetches the ABI of a verified smart contract from Etherscan.

        Args:
            contract_address (str): The smart contract address.

        Returns:
            list: ABI if found, otherwise None.
        """
        url = ETHERSCAN_GET_ABI_ENDPOINT.format(address=contract_address)
        response = requests.get(url)
        data = response.json()

        if data["status"] == "1":
            return json.loads(data["result"])
        logger.error(f"Failed to fetch ABI for {contract_address} from Etherscan.")
        return None

    def load_abi_from_file(self, abi_path: str) -> list:
        """
        Loads a smart contract ABI from a JSON file.

        Args:
            abi_path (str): The file path to the ABI JSON.

        Returns:
            list: The loaded ABI.
        """
        if not os.path.exists(abi_path):
            raise FileNotFoundError(f"ABI file not found: {abi_path}")
        with open(abi_path, "r") as file:
            return json.load(file)

    def save_abi_to_json(self, contract_address: str, file_name: str, save_path: str):
        """
        Fetches the ABI of a given contract from Etherscan and saves it as a JSON file.

        Args:
            contract_address (str): Address of the contract.
            file_name (str): Name of the JSON file to save (without .json extension).
            save_path (str): Directory where the file should be saved.

        Returns:
            str: Full path of the saved ABI file, or None if failed.
        """
        abi = self.fetch_abi_from_etherscan(contract_address)
        if not abi:
            return None

        os.makedirs(save_path, exist_ok=True)
        full_file_path = os.path.join(save_path, f"{file_name}.json")

        with open(full_file_path, "w") as json_file:
            json.dump(abi, json_file, indent=4)

        logger.info(f"ABI for {contract_address} saved to {full_file_path}")
        return full_file_path
