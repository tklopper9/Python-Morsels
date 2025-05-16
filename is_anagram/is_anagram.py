from collections import Counter

def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ","")
    str1 = filter(str.isalpha, str1)
    str2 = str2.lower().replace(" ","")
    str2 = filter(str.isalpha, str2)
    
    if Counter(str1) == Counter(str2):
        return True
    else:
        return False