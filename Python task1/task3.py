def isPalindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


str = input("Enter string to check whether is it a palindrome or not")
ans = isPalindrome(str)

if (ans):
    print("Yes")
else:
    print("No")

if ans=="Yes":
    for i in range(len(str)):
        str[i]=hex
        hex=char_to_hex_string(s)
        print(hex)

elif ans=="No":
    for i in range(0, len(str)):
        print(" " * (len(str) - i - 1), end="")
        for k in range(0, i + 1):
            print(str[k], end="")
        for j in range(i, 0, -1):
            print(str[j - 1], end="")
        print("")

    for i in range(len(str) - 2, -1, -1):
        print(" " * (len(str) - i - 1), end="")
        for j in range(0, i + 1):
            print(str[j], end="")
        for k in range(i, 0, -1):
            print(str[k - 1], end="")
        print("")

else:
    print("invalid charecters entered")


