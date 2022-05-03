"""
Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'

If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
The shift will always be in range of [1, 26].
"""

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.ab = "abcdefghijklmnopqrstuvwxyz"

    def encode(self, st):
        print(len(st), st)
        result = ""
        for i in st.lower():
            if i not in self.ab:
                result += i
                continue
            shifted = (self.ab.find(i) + self.shift) % (len(self.ab))
            print(shifted)
            result += self.ab[shifted].upper()
        return result
        
    def decode(self, st):
        self.shift *= -1
        result = self.encode(st)
        self.shift *= -1
        return result