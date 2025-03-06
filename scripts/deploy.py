# SPDX-License-Identifier: BUSL-1.1
import os

from ape import project, accounts, networks


def main():
    contract_name = str(os.getenv("CONTRACT")).lower()
    networks.parse_network_choice("base:sepolia")
    chain_id = os.getenv("CHAIN_ID")
    publish = os.getenv("PUBLISH", True)
    cont = os.getenv(f"SLIPSTREAM_HELPER_{chain_id}")
    account = None
    print(f"On chain id: {chain_id}, :: {contract_name}, {cont}++")

    if os.getenv("PROD"):
        account = accounts.load("sugar")
    elif len(accounts) > 0:
        account = accounts[0]
        print(f"Using account: {account.address}")

    if "lp" in contract_name:
        project.LpSugar.deploy(
            os.getenv(f"VOTER_{chain_id}"),
            os.getenv(f"REGISTRY_{chain_id}"),
            os.getenv(f"CONVERTOR_{chain_id}"),
            os.getenv(f"SLIPSTREAM_HELPER_{chain_id}"),
            os.getenv(f"ALM_FACTORY_{chain_id}"),
            sender=account,
            publish=publish,
            api_key="5IXHGRSRBJAUG5URPDJXPV6DPMSY648UK8"
        )

    elif "rewards" in contract_name:
        project.RewardsSugar.deploy(
            os.getenv(f"VOTER_{chain_id}"),
            os.getenv(f"REGISTRY_{chain_id}"),
            os.getenv(f"CONVERTOR_{chain_id}"),
            sender=account,
            publish=publish,
        )

    elif "ve" in contract_name:
        project.VeSugar.deploy(
            os.getenv(f"VOTER_{chain_id}"),
            os.getenv(f"DIST_{chain_id}"),
            os.getenv(f"GOVERNOR_{chain_id}"),
            sender=account,
            publish=publish,
        )

    elif "relay" in contract_name:
        project.RelaySugar.deploy(
            str(os.getenv(f"RELAY_REGISTRY_ADDRESSES_{chain_id}")).split(","),
            os.getenv(f"VOTER_{chain_id}"),
            sender=account,
            publish=publish,
        )

    elif "registry" in contract_name:
        project.FactoryRegistry.deploy(
            str(os.getenv(f"FACTORIES_{chain_id}")).split(","),
            str(os.getenv(f"REWARDS_FACTORIES_{chain_id}")).split(","),
            str(os.getenv(f"GAUGE_FACTORIES_{chain_id}")).split(","),
            str(os.getenv(f"INIT_HASHES_{chain_id}")).split(","),
            sender=account,
            publish=publish,
        )

    else:
        print("Set the `CONTRACT` environment variable to deploy a contract.")
