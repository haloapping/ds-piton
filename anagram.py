from collections import Counter
from ctypes import Union


def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s1_dict = Counter(s1)
    s2_dict = Counter(s2)

    for key in s1_dict.keys():
        is_key_not_exist = s2_dict.get(key, None) == None
        is_counter_not_same = s1_dict.get(key, None) != s2_dict.get(key, None)

        if is_key_not_exist and is_counter_not_same:
            return False

    return True


print(is_anagram("apping", "ganteng"))
Uni