# DeFi Data Collectors

## Overview
DeFi Data Collectors is a **modular, open-source data pipeline** for fetching raw on-chain data from various DeFi protocols. It provides **institutional-grade** data collection for **Risk Engine** and other blockchain analytics projects.

## Supported Data Sources
- **Aave** – Fetches collateral prices, loan values, and liquidation thresholds across networks.
- **More protocols coming soon...**

## Project Structure
```
defi-data-collectors/
│── collectors/             # Protocol-based data collectors
│   ├── base_fetcher.py     # Base class for shared Web3 & ABI logic
│   ├── aave_fetcher.py     # Aave-specific data collector
│   ├── __init__.py
│
│── config/                 # Configurations and setup
│   ├── onchain_infra.py    # Manages Web3 instance, RPCs, and API keys
│   ├── logger.py           # Centralized logging (UTC+0 timestamps)
│   ├── __init__.py
│
│── protocols/              # Protocol-specific configurations
│   ├── aave.py             # Aave contract addresses & parameters
│   ├── __init__.py
│
│── tests/                  # Unit tests
│── requirements.txt        # Dependencies
│── README.md               # Documentation
│── .gitignore              # Ignore unnecessary files
```

## Installation

### Standalone Usage
```bash
git clone https://github.com/yourusername/defi-data-collectors.git
cd defi-data-collectors
pip install -r requirements.txt
```

### Using with Risk Engine
DeFi Data Collectors is designed to work with **[Risk Engine](https://github.com/GeorgeVSV/defi-risk-engine)** as a submodule.

If you're using this inside **Risk Engine**, update the submodule:
```bash
cd risc-engine
git submodule update --remote
```

## How to Use

### 1. Fetch Aave Data
```python
from collectors.aave_fetcher import AaveFetcher

aave_fetcher = AaveFetcher()
aave_pool = aave_fetcher.get_aave_contract(network="ethereum", market_type="core_market", contract_type="pool")
```
