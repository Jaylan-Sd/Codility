# Given a string, find the first character that does not repeat anywhere in the string. Return None if all characters repeat.



# Input: "Hello"

# Output: "H"
# Input: "Swiss"
# Output: "w"


def first_non_repeating_char(word):
    counts = {}

    for letter in word:
        if letter not in counts:
            counts[letter] = 1

        else:
            counts[letter] += 1    

    for letter in word:
        if counts[letter] == 1:
            return letter
                    

    return None 



print(first_non_repeating_char("Hello"))
print(first_non_repeating_char("Swiss"))  
