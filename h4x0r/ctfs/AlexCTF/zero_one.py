import base64
with open('zero_one') as f:
    file_c = f.read()
buffer = ''
output = ''

for x in file_c:
    if x == ' ':
        continue
    buffer += x
    if buffer == 'ZERO':
        output += '0'
        buffer = ''
    elif buffer == 'ONE':
        output += '1'
        buffer = ''

final = ''
for x in range(0, len(output), 8):
    bin = output[x:x+8]
    bin = int(bin, 2)
    final += chr(bin)
print(final)
