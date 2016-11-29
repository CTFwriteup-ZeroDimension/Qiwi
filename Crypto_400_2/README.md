# Crypto_400_2
By factordb, we find that n is actually the square of a prime p. Then we can easily compute it's d = inv(e, p*(p-1)). Then we can get the message by c ** d % n.  
``` python3
from collections import defaultdict
import sympy
def inv(x, m):
    return int(sympy.invert(x, m))
def int_to_bytes(bigint):
    tmp, arr = bigint, []
    while tmp > 0:
        arr.append(tmp & 0xff)
        tmp >>= 8
    arr = arr[::-1]
    return bytes(arr)
with open('message.txt', 'r') as fp:
    n = int(fp.readline().strip().split('=')[1])
    e = int(fp.readline().strip().split('=')[1])
    c = int(fp.readline().strip().split('=')[1])
p = int('12576521404814116418405527293372462493644446561744586896117484752900970475678321656709800103835040670074114354485616047706006446067458303134493822198866717')
phi_n = p * (p-1)
d = inv(e, phi_n)
print('flag:', int_to_bytes(pow(c, d, n)).decode('utf8'))
```
