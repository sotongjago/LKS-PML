FLAG = b"LKSPML{xor_1s_w34k_1f_r3us3d}"
KEY  = b"crypto"

def xor(data, key):
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))

cipher = xor(FLAG, KEY)

with open("cipher.bin", "wb") as f:
    f.write(cipher)

print("cipher.bin generated")
