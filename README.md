# DeFi Data Collectors

## Overview
DeFi Data Collectors is a **modular, open-source data pipeline** for fetching raw on-chain data from various DeFi protocols. It provides **institutional-grade** data collection for **Risk Engine** and other blockchain analytics projects.

## Supported Data Sources
- **Aave** – Fetches collateral prices, loan values, and liquidation thresholds.
- **More protocols coming soon...**

## Project Structure
```
defi-data-collectors/
│── collectors/             # Data collection modules
│   ├── aave_fetcher.py     # Fetches Aave data
│   ├── __init__.py
│
│── tests/                  # Unit tests for collectors
│── requirements.txt         # Dependencies
│── README.md                # Documentation
│── .gitignore               # Ignore unnecessary files
```

## Installation
### Standalone Usage
```bash
git clone https://github.com/yourusername/defi-data-collectors.git
cd defi-data-collectors
pip install -r requirements.txt
```

### Using with Risk Engine
DeFi Data Collectors is designed to work with **[Risk Engine](https://github.com/GeorgeVSV/defi-risk-engine.git)** as a submodule.

If you're using this inside **Risk Engine**, update the submodule:
```bash
cd risc-engine
git submodule update --remote
```

## Contributing
Contributions are welcome! If you'd like to add new data collectors, open a PR or discussion.

## License
[MIT License](LICENSE)
