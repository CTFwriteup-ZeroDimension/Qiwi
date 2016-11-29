cipher = [[[int(y) for y in x[idx: idx+2]] for idx in range(0, len(x), 2)] for x in '52112515 4535 331534 442315 321144422453 231143 543445 213431313452 442315 5223244415 411112122444 2533341325 2533341325 331534 442315 21311122 2443 442315 4423244214 31243315'.split(' ')]
#print(cipher)

play_fare = ['ABCDE', 'FGHIK', 'LMNOP', 'QRSTU', 'VWXYZ']
message = []
for c in cipher:
    word = []
    for x in c:
        word.append(play_fare[x[0]-1][x[1]-1])
    message.append(''.join(word))
print(' '.join(message))
