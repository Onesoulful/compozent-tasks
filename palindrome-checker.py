def isPalindrome(s):
    return s == s[::-1]

s = str(input("The word is "))
ans = isPalindrome(s)
print(ans)

if ans:
    print("Yes")
else:
    print("No")