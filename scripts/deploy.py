from brownie import OurToken
from scripts.helpful_scripts import get_account
from web3 import Web3

supply = Web3.toWei(1000, "ether")


def deploy_token():
    account = get_account()
    token = OurToken.deploy(
        supply,
        {"from": account},
    )
    print(f"Deployed {token.name()}")
    return token


def main():
    deploy_token()
