from brownie import (
    accounts,
    config,
    network,
    Contract,
)

LOCAL_BLOCKCHAINS = ["development", "ganache-local"]
LOCAL_BLOCKCHAIN_FORKS = ["mainnet-fork", "mainnet-fork-dev"]
ALL_LOCAL_BLOCKCHAINS = LOCAL_BLOCKCHAIN_FORKS + LOCAL_BLOCKCHAINS


def get_account(index=None, id=None) -> str:
    ### accounts[0]
    # accounts.add(env)
    # accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in ALL_LOCAL_BLOCKCHAINS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
