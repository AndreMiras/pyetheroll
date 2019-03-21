from distutils.core import setup

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
setup(name='pyetheroll',
      version='20181031',
      description='Python library to Etheroll smart contract',
      author='Andre Miras',
      url='https://github.com/AndreMiras/pyetheroll',
      packages=['pyetheroll'],
      install_requires=install_requires,
      dependency_links=dependency_links)
