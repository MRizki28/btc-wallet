import os
import json
from bitcoinlib.wallets import wallet_create_or_open
from bitcoinlib.mnemonic import Mnemonic

wallet_name = input("Masukkan nama wallet: ").strip()

mnemo = Mnemonic('english')
mnemonic_phrase = mnemo.generate(strength=256)

wallet = wallet_create_or_open(
    wallet_name,
    keys=mnemonic_phrase,
    network='bitcoin',
    witness_type='segwit'
)

key = wallet.new_key()
address = key.address
wif_private_key = key.wif

output_dir = "wallet_files"
os.makedirs(output_dir, exist_ok=True)

wallet_data = {
    "wallet_name": wallet_name,
    "mnemonic": mnemonic_phrase,
    "address": address,
    "wif_private_key": wif_private_key
}

with open(f"{output_dir}/{wallet_name}.json", "w") as f:
    json.dump(wallet_data, f, indent=4)

print(f"\n✅ Wallet berhasil dibuat dan disimpan ke file: {output_dir}/{wallet_name}.json")
