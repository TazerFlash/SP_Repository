fileHand = open("names.csv")

nameDict = {}

for line in fileHand:
    nameList = line.strip().split(",")
    if len(nameList) == 2:
        key, value = int(nameList[0]), nameList[1]
        nameDict[key] = value  # Creating name dictionary

strDict = nameDict.copy()
nameStr = ""
diff = 10000

print("The sorted list is:\n")
for key, value in sorted(nameDict.items()):
    print("{}: {}".format(key, nameDict[key]))  # Sorting and printing the dictionary

for key, value in list(nameDict.items()):
    if int(key) % 2 != 0:
        nameDict.pop(key)  # Removing odd numbered rows.

print("\nThe even-only sorted list is:\n")
for key, value in sorted(nameDict.items()):
    print("{}: {}".format(key, nameDict[key]))  # Printing new even only list.

for key, value in nameDict.items():
    nameStr += value

for i in range(len(nameStr)):
    for j in range(len(nameStr)):
        if ord(nameStr[i]) != ord(nameStr[j]):
            if abs(ord(nameStr[i]) - ord(nameStr[j])) < diff:
                diff = abs(ord(nameStr[i]) - ord(nameStr[j]))
            else:
                continue
        else:
            continue  # Finding minimum ASCII difference

print("\nThe minimum ASCII difference is:", diff)