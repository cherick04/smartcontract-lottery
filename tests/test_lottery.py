from brownie import Lottery, network, accounts, config
from web3 import Web3

# 1 ETH = 4000 USD
# 50 USD = 0.0125 ETH
# 12500000000000000


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    assert lottery.getEntranceFee() > Web3.toWei(0.012, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.013, "ether")
