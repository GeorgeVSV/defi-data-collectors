from collectors.base_fetcher import BaseFetcher
from config.protcols.aave import AAVE_CONFIG
from config.logger import get_logger

logger = get_logger()

class AaveFetcher(BaseFetcher):
    """
    Fetcher for Aave V3 smart contracts.
    Handles data providers and specific contract interactions.
    """

    def get_aave_contract(self, network: str, market_type: str, contract_type: str):
        """
        Retrieves a specific Aave contract.

        Args:
            network (str): Blockchain network (e.g., "ethereum").
            market_type (str): Aave market type (e.g., "core_market").
            contract_type (str): Contract type (e.g., "pool", "oracle").

        Returns:
            Web3.eth.Contract: Web3 contract instance.
        """
        if network not in AAVE_CONFIG:
            raise ValueError(f"Aave network '{network}' not found in config.")

        market_data = AAVE_CONFIG[network].get(market_type)
        if not market_data or contract_type not in market_data:
            raise ValueError(f"Aave contract '{contract_type}' not found in '{market_type}' on {network}.")

        contract_address = market_data[contract_type]
        abi = self.fetch_abi_from_etherscan(contract_address)
        logger.info(f"Fetched '{contract_type}' contract for Aave on {network}: {contract_address}")

        return self.get_contract(contract_address, abi)
