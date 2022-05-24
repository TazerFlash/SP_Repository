from binascii import unhexlify

def brute(input, key):
    if len(input) != len(key):
        return "Failed!"

        output = b''

        for b1, b2 in zip(input, key):
            output += bytes([b1 ^ b2])

        try:
            return output.decode("utf-8")
        except:
            return "Cannot decode some bytes"

a = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
b = unhexlify(data)
print("[-] CIPHER: {}".format(b))

key_part = brute(b[:7], "crypto{".encode())
print("[-] PARTIAL KEY FOUND: {}".format(key_part))

key = (key_part + "y").encode()
key += key * int((len(cipher) - len(key))/len(key)
key += key[:((len(cipher) - len(key))%len(key))]
print("[-] Decoding using KEY: {}".format(key))

plain = brute(cipher, key)
print("\n[*] FLAG: {}".format(plain))
