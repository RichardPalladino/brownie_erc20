from time import sleep

from brownie import exceptions, config, network, TRILLToken

from scripts.deploy_trill import deploy_trill_token
from scripts.helper_scripts import get_account


def test_deployment():
    # arrange
    # account = get_account()
    # act
    trill_token = deploy_trill_token(supply=7357000000000000000000)
    # assert
    assert trill_token.totalSupply == 7357000000000000000000
