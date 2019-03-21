import os

from setuptools import setup

install_requires = [
    'eth-account',
    'eth-utils',
    'py-etherscan-api==0.8.0',
    'pycryptodome',
    'requests-cache',
    'rlp',
    'web3',
]
dependency_links = [
    ('https://github.com/corpetty/py-etherscan-api'
     '/archive/3c68b57.zip#egg=py-etherscan-api-0.8.0'),

]


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(name='pyetheroll',
      version='20190321',
      description='Python library to Etheroll smart contract',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      author='Andre Miras',
      url='https://github.com/AndreMiras/pyetheroll',
      packages=['pyetheroll'],
      install_requires=install_requires,
      dependency_links=dependency_links)
