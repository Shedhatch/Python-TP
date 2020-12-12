def is_palindrome(a):
    for i in range(len(a)//2):
        if a[i] != a[-i-1]:
            return False
    return True

a = input('Saisir une chaîne de caractères sans accents, ponctuation, espaces ou majuscules: \n')
if is_palindrome(a) == True:
    print("Ceci est un palindrome.")
else:
    print("Ceci n'est pas un palindrome.")