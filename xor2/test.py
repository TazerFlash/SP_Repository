from pwn import xor

a = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
a2b = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
b2c = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

b = xor(bytes.fromhex(a2b), a)
c = xor(bytes.fromhex(b2c), b)
d = xor(bytes.fromhex(a2b), c)

keyflag = xor(bytes.fromhex(flag), d)

print(keyflag)
