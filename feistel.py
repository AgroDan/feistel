#!/usr/bin/env python3


def jumble(obj):
    """
        Jumbles the provided object somehow
    """
    if type(obj) is str:
        obj = obj.encode('utf-8')

    return obj[::-1]


def enc(obj, key):
    """
        Completely messes around the object
        and xors it with the key. The key must
        be one byte long!
    """
    if type(obj) is str:
        obj = obj.encode('utf-8')

    if type(key) is bytes:
        key = ord(key)

    # e = [key^i for i in obj]
    return bytes([((i**2)-1)%256 for i in [key^i for i in obj]])


def feistel(data, key, rounds=20, method='encrypt'):
    """
        Using a feistel network, jumbles data and returns output.
    """
    if type(data) is str:
        data = data.encode('utf-8')

    if type(key) is str:
        key = key.encode('utf-8')

    if method not in ('encrypt', 'decrypt', 'e', 'd'):
        raise Exception('Allowed methods: Encrypt or Decrypt!')

    if method in ('decrypt', 'd'):
        key = key[::-1]

    # TODO: Figure out how to create a UFN
    if len(data)%2:
        data += b'\x00'

    half = len(data) // 2
    left = data[:half]
    right = data[half:]

    for r in range(rounds):
        for k in key:
            e = enc(right, k)
            f = [i^j for i,j in zip(e,left)]
            left = right
            right = bytes(f)

    res = right+left
    if res[-1] == 0x0:
        res = res[:-1]
    return res
