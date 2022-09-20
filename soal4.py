kalimat = ['madam']

def is_palindrome(x):
    if x == x[::-1]:
        print(True)
    else:
        print(False)

print(list(filter(is_palindrome,kalimat)))
