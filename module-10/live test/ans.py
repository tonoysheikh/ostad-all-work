def is_palindrome(s):
    temp = s[::-1]
    if temp == s :
        return True
    else:
        return False


def show_palindromic_substrings(s):
    res = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            res.append(s[i:j])
 

    print(str(res))
        

s = input()

print(is_palindrome(s))
show_palindromic_substrings(s)

