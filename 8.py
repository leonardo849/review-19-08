def isPalindrome(word):
    wordLower = word.lower().replace(" ", "")
    wordReversed = wordLower[::-1]
    return wordLower == wordReversed

print(isPalindrome("batman"))