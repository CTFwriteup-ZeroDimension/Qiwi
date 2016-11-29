# Crypto_400_1
e = 3 and the message(m) is encrypted three times with different key.  
Write up the relation:  
(m ** 3) % n1 = c1  
(m ** 3) % n2 = c2  
(m ** 3) % n3 = c3  
It's actually the Chinese Remainder Theorem.  
Using sympy solve m**3 and find m by binary search.  
We get flag: theoretical_computer_scientist_johan_torkel_hastad

``` python3 
from collections import defaultdict
import sympy
from sympy.ntheory.modular import crt
def inv(x, m):
    return sympy.invert(x, m)
def nth_root(x, n):
    right = 1
    while right ** n <= x:
        right *= 2
    left = right // 2
    while left < right:
        mid = (left + right) // 2
        if left < mid and mid ** n < x:
            left = mid
        elif right > mid and mid ** n > x:
            right = mid
        else:
            return mid
    return False
def int_to_bytes(bigint):
    tmp, arr = bigint, []
    while tmp > 0:
        arr.append(tmp & 0xff)
        tmp >>= 8
    arr = arr[::-1]
    return bytes(arr)

with open('message.txt', 'r') as fp:
    n1 = fp.readline().strip().split('=')[1]
    c1 = fp.readline().strip().split('=')[1]
    n2 = fp.readline().strip().split('=')[1]
    c2 = fp.readline().strip().split('=')[1]
    n3 = fp.readline().strip().split('=')[1]
    c3 = fp.readline().strip().split('=')[1]
flag = crt([int(x) for x in (n1, n2, n3)], [int(x) for x in (c1, c2, c3)])[0]
flag = nth_root(flag, 3)
print('flag:', int_to_bytes(flag).decode('utf8'))
```
