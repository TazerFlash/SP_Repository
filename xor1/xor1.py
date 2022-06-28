text = "label"
result = ""

for n in text:
    result = chr(ord(n)^13)
    print(result)
