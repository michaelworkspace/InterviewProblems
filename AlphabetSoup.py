"""Alphabet Soup Algorithm:

Problem: Given a string of alphabetical characters following the rules seen down below in part A and part B,
return a new string with the characters in the alphabetical order. Capital letters should appear before the same lowercase
letter(s) in part B e.g. (aBbbCcdEe...). There will be no spaces in any of the strings.

Part A) The string contains only lowercase letters
Part B) The string contans both lowercase and uppercase letters

Sample Input/Output:

A) 'hello' -> 'ehllo'
B) 'eLEPhAnt' -> 'AEehLnPt' 

"""

input_a = 'hello'
input_b = 'eLEPhAnt'


def alphapetize(word: str) -> str:
    """Returns a sorted string with capital letters in front of it's lowercase counterparts."""

    sorted_word = sorted(word)

    cap_letters = []
    lower_word = sorted(word.lower())
    new_word = []

    for letter in sorted_word:
        if letter.isupper():
            cap_letters.append(letter)

    for letter in lower_word:
        if letter.upper() in cap_letters:
            new_word.append(letter.upper())
            cap_letters.remove(letter.upper())
        else:
            new_word.append(letter)

    new_word = "".join(new_word)

    return new_word


assert alphapetize(input_a) == 'ehllo'
assert alphapetize(input_b) == 'AEehLnPt'

print(alphapetize(input_b))
