from nostr.key import PrivateKey

private_key = PrivateKey()
public_key = private_key.public_key
print("\n")
print(f"Private key:  {private_key.bech32()}")
print(f"Public key: {public_key.bech32()}")
print("\n")

