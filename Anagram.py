# Check if two strings are anagrams

def _is_anagram(s1,s2):
    return set(s1) == set(s2)


print(is_anagram("Ruslan","Anar"))
