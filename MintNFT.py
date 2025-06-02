import json
import time
import itertools
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from eth_utils import to_checksum_address

RPC = "https://gotchipus.com/api/testnet"
EXPLORER = "https://testnet.pharosscan.xyz/tx/"
CONTRACT_ADDRESS = "0x0000000038f050528452d6da1e7aacfa7b3ec0a8"
CHAIN_ID = 0xa8230
MINT_FUNCTION_SELECTOR = "0x5b70ea9f"
MAX_RETRY = 50
DELAY_WALLET = 5  
DELAY_RETRY = 1

def print_banner():
    banner = """
╭─────────────── Testnet Tools - Pharos Mint NFT ───────────────╮
│                                                               │
│ ████████╗███████╗███████╗████████╗███╗   ██╗███████╗████████╗ │
│ ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝████╗  ██║██╔════╝╚══██╔══╝ │
│    ██║   █████╗  ███████╗   ██║   ██╔██╗ ██║█████╗     ██║    │
│    ██║   ██╔══╝  ╚════██║   ██║   ██║╚██╗██║██╔══╝     ██║    │
│    ██║   ███████╗███████║   ██║   ██║ ╚████║███████╗   ██║    │
│    ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝    │
│                                                               │
╰─────────────────────── BY ADFMIDN TEAM ───────────────────────╯
"""
    print(banner)

def read_file(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def load_minted_data(filename="datanft.txt"):
    minted = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                if ":" in line:
                    pk, addr = line.strip().split(":", 1)
                    minted[pk.strip()] = addr.strip()
    except FileNotFoundError:
        pass
    return minted

def save_minted_data(private_key, address, filename="datanft.txt"):
    with open(filename, "a") as f:
        f.write(f"{private_key} : {address}\n")

def wait_for_tx(w3, tx_hash, timeout=60):
    print("   ⏳ Menunggu transaksi diproses...", end="", flush=True)
    for _ in range(timeout):
        try:
            tx = w3.eth.get_transaction(tx_hash)
            if tx and tx['blockHash'] != Web3.to_bytes(hexstr="0x0"):
                print("\n   ✅ Transaksi dikonfirmasi.")
                return True
        except:
            pass
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n   ❌ Transaksi tidak muncul setelah timeout.")
    return False

def mint_nft(w3, pk):
    acct = Account.from_key(pk)
    address = acct.address
    checksum_address = to_checksum_address(address)

    print(f"   📬 Address \t\t: {checksum_address}")

    for attempt in range(1, MAX_RETRY + 1):
        try:
            nonce = w3.eth.get_transaction_count(checksum_address)
            balance_wei = w3.eth.get_balance(checksum_address)
            balance_phrs = w3.from_wei(balance_wei, 'ether')
            print(f"   💰 Balance PHRS \t: {balance_phrs:.4f}")

            if balance_phrs == 0:
                print("   ⚠️  Balance 0 PHRS, kemungkinan belum faucet.")
                return None
            break  
        except Exception as e:
            if attempt < MAX_RETRY:
                time.sleep(DELAY_RETRY)
            else:
                print("   ❌ Gagal koneksi setelah beberapa percobaan.")
                return None  

    for attempt in range(1, MAX_RETRY + 1):
        try:
            gas_price = w3.eth.gas_price

            txn = {
                'to': to_checksum_address(CONTRACT_ADDRESS),
                'from': checksum_address,
                'value': 0,
                'gas': 300000,
                'gasPrice': gas_price,
                'nonce': nonce,
                'chainId': CHAIN_ID,
                'data': MINT_FUNCTION_SELECTOR,
            }

            signed_txn = w3.eth.account.sign_transaction(txn, private_key=pk)
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash_hex = tx_hash.hex()

            print(f"   🔁 Attempt {attempt}: Mint NFT terkirim.")

            if wait_for_tx(w3, tx_hash_hex):
                print(f"   🔗 Explorer: {EXPLORER}{tx_hash_hex}")
                return tx_hash_hex
            else:
                print("   ⚠️ Transaksi tidak terkonfirmasi, ")

        except Exception as e:
            time.sleep(DELAY_RETRY)

    print("   ❌ Gagal mint setelah beberapa percobaan.")
    return None

def assign_proxies(private_keys, proxies):
    if proxies:
        proxy_cycle = itertools.cycle(proxies)
        wallets = []
        for pk in private_keys:
            wallets.append({
                "private_key": pk,
                "proxy": next(proxy_cycle)
            })
    else:
        wallets = [{"private_key": pk, "proxy": None} for pk in private_keys]
    return wallets

def print_separator():
    print("=" * 60)

def main():
    print_banner()
    private_keys = read_file("privateKeys.txt")
    proxies = []
    try:
        proxies = read_file("proxy.txt")
    except FileNotFoundError:
        pass

    minted_data = load_minted_data()
    wallets = assign_proxies(private_keys, proxies)

    for idx, wallet in enumerate(wallets, 1):
        pk = wallet["private_key"]
        proxy = wallet["proxy"]

        print_separator()
        print(f"[{idx}] Memproses wallet")

        if pk in minted_data:
            print("   ✅ Sudah pernah mint. Lewati.")
            continue

        if proxy:
            w3 = Web3(Web3.HTTPProvider(RPC, request_kwargs={"proxies": {"http": proxy, "https": proxy}}))
            print(f"   🔗 Menggunakan proxy: {proxy}")
        else:
            w3 = Web3(Web3.HTTPProvider(RPC))
            print(f"   🔗 Tidak menggunakan proxy")

        w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        tx_hash = mint_nft(w3, pk)
        if tx_hash:
            acct = Account.from_key(pk)
            save_minted_data(pk, acct.address)

        print(f"   ⏳ Delay {DELAY_WALLET}s sebelum ke wallet berikutnya...")
        time.sleep(DELAY_WALLET)
    print_separator()

if __name__ == "__main__":
    main()
