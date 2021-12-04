from setuptools import setup

dependencies = [
    "multidict==5.1.0",  # Avoid 5.2.0 due to Avast
    "blspy==1.0.7",  # Signature library
    "chiavdf==1.0.3",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.4",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.15",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the chives processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspythonchia==2.2.0",  # Query DNS seeds
    "packaging==21.0",
    "watchdog==2.1.6",  # Filesystem event watching - watches keyring.yaml
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "types-setuptools",
]

kwargs = dict(
    name="chives-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@chivescoin.org",
    description="Chives blockchain full node, farmer, timelord, and wallet.",
    url="https://chivescoin.org/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="chives blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "chives",
        "chives.cmds",
        "chives.clvm",
        "chives.consensus",
        "chives.daemon",
        "chives.full_node",
        "chives.timelord",
        "chives.farmer",
        "chives.harvester",
        "chives.introducer",
        "chives.plotting",
        "chives.pools",
        "chives.protocols",
        "chives.rpc",
        "chives.server",
        "chives.simulator",
        "chives.types.blockchain_format",
        "chives.types",
        "chives.util",
        "chives.wallet",
        "chives.wallet.puzzles",
        "chives.wallet.rl_wallet",
        "chives.wallet.cc_wallet",
        "chives.wallet.did_wallet",
        "chives.wallet.settings",
        "chives.wallet.trading",
        "chives.wallet.util",
        "chives.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "chives = chives.cmds.chives:main",
            "chives_wallet = chives.server.start_wallet:main",
            "chives_full_node = chives.server.start_full_node:main",
            "chives_harvester = chives.server.start_harvester:main",
            "chives_farmer = chives.server.start_farmer:main",
            "chives_introducer = chives.server.start_introducer:main",
            "chives_timelord = chives.server.start_timelord:main",
            "chives_timelord_launcher = chives.timelord.timelord_launcher:main",
            "chives_full_node_simulator = chives.simulator.start_simulator:main",
        ]
    },
    package_data={
        "chives": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "chives.util": ["initial-*.yaml", "english.txt"],
        "chives.ssl": ["chives_ca.crt", "chives_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
