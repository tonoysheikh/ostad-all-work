s = input()

res = False
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        res = True

if res:
    print("The string contains a vowel.")
else:
    print("The string does not contain any vowel.")