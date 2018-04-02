import base64
ct = 'GCg7Ozs7Oy01e3oNMz4gP3ogP3ovPjs2NXoZM3opMz96KDUgKSAjPCg1LTs5ei4/MSkueiA7KSAjPCg1LTs0I3oqNTA/PiM0OSAjN3o4OzAuPzd0ehQ1ej41OCg7dno8Njs9O3ouNWB6CBUADRsWBSEJMzQ9Nj8CNSgYIy4/GTMqMj8oJw=='

tries = []

for x in [ 2**a for a in range(0,7) ]:
    tries.append(''.join( [ chr( ord(y) ^ x ) for y in ct ] ))

for dt in tries:
    try:
        print( str(base64.b64decode(dt)) )
    except:
        print('=============RIP============')


