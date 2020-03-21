import os

from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


# exposing the params so it can be imported
setup_params = {
    "name": "pyetheroll",
    "version": "20200320",
    "description": "Python library to Etheroll smart contract",
    "long_description": read("README.md"),
    "long_description_content_type": "text/markdown",
    "author": "Andre Miras",
    "url": "https://github.com/AndreMiras/pyetheroll",
    "packages": ["pyetheroll"],
    "install_requires": [
        "eth-account<0.5",
        "eth-utils",
        "py-etherscan-api==0.8.0",
        "pycryptodome",
        "requests-cache",
        "rlp",
        "web3<6",
    ],
    "dependency_links": [
        (
            "https://github.com/corpetty/py-etherscan-api"
            "/archive/3c68b57.zip#egg=py-etherscan-api-0.8.0"
        )
    ],
}


def run_setup():
    setup(**setup_params)


# makes sure the setup doesn't run at import time
if __name__ == "__main__":
    run_setup()
