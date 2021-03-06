from typing import Dict

# The rest of the codebase uses mojos everywhere.
# Only use these units for user facing interfaces.
units: Dict[str, int] = {
    "chives": 10 ** 8,  # 1 chives (XCH) is 1,000,000,000,000 mojo (1 trillion)
    "mojo": 1,
    "colouredcoin": 10 ** 3,  # 1 coloured coin is 1000 colouredcoin mojos
}
