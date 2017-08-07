#! python

import string

def reverse(text):
    return text[::-1]

#text must be str
def isPalindrome(text):
    text = text.lower()
    text = text.replace(' ', '')

    for i in string.punctuation:
        text = text.replace(i, '')

    return text == reverse(text)

def main():
    text = input("Enter a word or sentence:")
    if isPalindrome(text):
        print("yes, it's palindrome")
    else:
        print("no, it's not")


if __name__ == "__main__":
    main()
else:
    print("palindrome was imported")