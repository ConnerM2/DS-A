"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
"""

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)

    # loops through each string in list
    for s in strs:
        # makes a list with 26 0's, each representing letter in the alphebet
        count = [0] * 26
        # loops through each character in each string
        for c in s:
            # using ascii, this gives you the index of each letter
            # a - a = 0; b - a = 1; ... z - a = 25
            # Then increases that index value by one
            count[ord(c) - ord('a')] += 1
        # adds that new list [1, 0, 0, 0, 1...] with the appropriate string into res
        res[tuple(count)].append(s)
    # gives back all the values; this case being the strings
    return list(res.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))


# This is same solution just shows how the dictionary grows over time
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)  # key: character count tuple, value: list of words

    for s in strs:
        count = [0] * 26  # one slot for each letter a–z
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        key = tuple(count)
        print(f"Word: '{s}' -> Count Key: {key}")
        
        res[key].append(s)
        print(f"Current Groups: {dict(res)}\n")  # Show how the dictionary is building

    result = list(res.values())
    print("Final Grouped Anagrams:", result)
    return result

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])