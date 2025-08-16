# 💬 Question: Count Vowels and Consonants

# Write a function that takes a string as input and returns the number of vowels and consonants in the string. You should ignore non-alphabetic characters (such as digits, punctuation, and spaces), and treat uppercase and lowercase letters as the same.

def countVowelsAndConsonants(s: str) -> Tuple[int, int]:
    vowels = 'aeiou'
    con = vow = 0
    for c in s.lower():
        if c.isalpha():
            if c in vowels:
                vow += 1
            else:
                con += 1
    return (vow, con)
