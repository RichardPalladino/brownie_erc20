from brownie import TRILLToken, config, network

from scripts.helper_scripts import get_account


def deploy_trill_token(supply=369000000000000000000000000, account=None):
    if account is None:
        account = get_account()
    print(f"Deploying the TrillToken contract to {network.show_active()}")
    trill_token = TRILLToken.deploy(
        supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Contract deployed successfully!")
    print(trill_token.totalSupply())
    return trill_token


def main() -> None:
    deploy_trill_token()


if __name__ == "__main__":
    main()
