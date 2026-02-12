with open("cipher.bin", "rb") as f:
    cipher = f.read()

known = b"LKSPML{"

keystream = bytes(cipher[i] ^ known[i] for i in range(len(known)))

def find_key(cipher, known):
    for key_len in range(2, 16):
        key = bytes(cipher[i] ^ known[i] for i in range(key_len))
        plain = bytes(cipher[i] ^ key[i % key_len] for i in range(len(cipher)))
        if plain.startswith(b"LKSPML{") and plain.endswith(b"}"):
            return key
    return None

key = find_key(cipher, known)
print("Recovered key:", key)

flag = bytes(cipher[i] ^ key[i % len(key)] for i in range(len(cipher)))
print(flag.decode())
