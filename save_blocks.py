from collections import defaultdict, OrderedDict
from datetime import datetime
import json
import os
import asyncio
from spectred.SpectredClient import SpectredClient


## Helpers
async def get_blocks(rpc_client, low_hash):
    r = await rpc_client.request(
        "getBlocksRequest",
        params={
            "lowHash": low_hash,
            "includeTransactions": True,
            "includeBlocks": True,
        },
    )
    return r["getBlocksResponse"]


async def get_vspc(rpc_client, low_hash):
    r = await rpc_client.request(
        "getVirtualChainFromBlockRequest",
        params={
            "startHash": low_hash,
            "includeAcceptedTransactionIds": True,
        },
        timeout=60 * 60 * 1,  # seconds * minutes * hours
    )
    return r["getVirtualChainFromBlockResponse"]


async def get_dag_info(rpc_client):
    r = await rpc_client.request("getBlockDagInfoRequest")
    return r["getBlockDagInfoResponse"]


async def get_selected_tip(rpc_client):
    r = await rpc_client.request("GetSinkRequest")
    return r["GetSinkResponse"]["sink"]


## Main
async def main():
    rpc_client = SpectredClient("localhost", 18110)

    # Get pruning point hash
    dag_info = await get_dag_info(rpc_client)
    low_hash = dag_info["pruningPointHash"]

    # Load blocks from pruning point hash to tip
    block_cache = OrderedDict()
    tx_to_blocks_index = defaultdict(list)

    while True:
        blocks = await get_blocks(rpc_client, low_hash)

        for idx, block in enumerate(blocks.get("blocks", [])):
            hash = block["verboseData"]["hash"]

            # Keep 1 level of parents for memory/storage purposes
            block["header"]["parents"] = block["header"]["parents"][0]["parentHashes"]
            # Add block to cache
            block_cache[hash] = block

            # Store tx to blocks mapping
            for tx in block["transactions"]:
                tx_id = tx["verboseData"]["transactionId"]
                tx_to_blocks_index[tx_id].append(hash)

            # Break once we get to DAG tip
            selected_tip = await get_selected_tip(rpc_client)
            if selected_tip == hash:
                break

            low_hash = hash

        last_cache_block = next(reversed(block_cache))
        selected_tip = await get_selected_tip(rpc_client)
        if selected_tip == last_cache_block:
            break

    # Keep an eye on progress
    os.system(
        "cls" if os.name == "nt" else "clear"
    )  # Clear console output (Windows: 'cls', others: 'clear')
    print(
        last_cache_block,
        datetime.fromtimestamp(
            int(block_cache[last_cache_block]["header"]["timestamp"]) / 1000
        ),
    )

    # Apply virtual selected parent chain to block_cache
    vspc_low_hash = next(iter(block_cache))
    vspc = await get_vspc(rpc_client, vspc_low_hash)

    # Block hash to stop VSPC iteration at to ensure accuracy
    vspc_stop_hash = None
    for k, v in reversed(block_cache.items()):
        if v["verboseData"]["isChainBlock"]:
            vspc_stop_hash = k
            break

    # Set isChainBlock to False for removed blocks
    for hash in vspc.get("removedChainBlockHashes", []):
        block_cache[hash]["verboseData"]["isChainBlock"] = False

    # Set isChainBlock to True for added blocks
    for hash in vspc.get("addedChainBlockHashes", []):
        if hash == vspc_stop_hash:
            break
        block_cache[hash]["verboseData"]["isChainBlock"] = True

    # Set accepted to True for accepted transactions
    tx_in_blocks_none = 0
    for d in vspc.get("acceptedTransactionIds", []):
        if d["acceptingBlockHash"] == vspc_stop_hash:
            break

        for accepted_tx_id in d["acceptedTransactionIds"]:
            tx_in_blocks = tx_to_blocks_index.get(accepted_tx_id)

            if tx_in_blocks is None:
                # TODO: Handle this case
                tx_in_blocks_none += 1
                continue

            for block_hash in tx_in_blocks:
                for i, tx in enumerate(block_cache[block_hash]["transactions"]):
                    if tx["verboseData"]["transactionId"] == accepted_tx_id:
                        tx["accepted"] = True
                        tx["acceptingBlockHash"] = d["acceptingBlockHash"]

    # Dump to JSON
    with open("./data/block2.json", "w") as f:
        json.dump({"blocks": block_cache}, f, indent=4)


# Run the main function
# Use an event loop for running the async main function
asyncio.run(main())
