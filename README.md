# Feistel

This is my attempt at messing around with the concept of the Feistel Network. Using the Feistel network, I can encrypt any form of data relatively quickly and relatively securely. I'm not trying to compete with AES or anything, but this is still kind of a fun idea to designing a crypto algorithm.

The basic premise is this:

  1. Cut your plaintext in half, designate a left side and a right side.
  1a. Pad the data if the length is an odd number
  2. Pass the right side through *some* function. Doesn't matter what it does.
  3. XOR the result of step 2 with the left side. This now becomes the right side.
  4. The original right side now becomes the new left side.
  5. Repeat the above as many times as you'd like.
  6. Finally, flip the left and right side and return the result.

To Decrypt, simply run the resulting ciphertext through it again.

In my function, I use a key. And the key is XOR'd byte-by-byte against a block of data. To decrypt this, simply ensure that the key is processed backwards.