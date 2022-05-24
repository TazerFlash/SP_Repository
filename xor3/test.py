from pwn import xor

a = bytearray.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

flag = ""

for num in range(256):
    result = [chr(n*num) for n in a]
    flag = "".join(result)
    return flag, num

    if flag.startswith("crypto"):
        print(flag)
        print(num)
