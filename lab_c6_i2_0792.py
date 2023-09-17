def isPalindrome(word):
    if(len(word) < 2):
        return True
    else:
        if(word[0] == word[-1]):
            return isPalindrome(word[1:-1])
        else:
            return False
inp = str(input('Enter Input : '))
if(isPalindrome(inp)):
    print('\'',inp,'\'',' is palindrome',sep='')
else:
    print('\'',inp,'\'',' is not palindrome',sep='')