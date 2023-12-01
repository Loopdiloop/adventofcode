import hashlib

# MD5 - hashes, starts with at least five 0s.

""" MD5 is a message-digest algorithm, widely used
and prduces a 128-bit hash value."""

input = "ckczppom"
found = False
i=0
while not found:
    string = input+str(i)
    hashed = hashlib.md5(string.encode())
    hexx = str(hashed.hexdigest())
    
    if hexx.startswith("000000"): # 5 or 6 zeros
        print("i for hash: ", i, hexx)
        found = True
    i += 1

