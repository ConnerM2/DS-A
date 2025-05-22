def longestCommonPrefix(strs: list[str]) -> str:
    # Empty string to store result
    res = ''
    # Loop through the length of the first string
    for i in range(len(strs[0])):
        # Loop through each string in strs
        for s in strs:
            # Checks if i is out of bounds; checks all strings at index i if they are the same
            if i == len(s) or s[i] != strs[0][i]:
                # if there is one that is not the same, res it returned
                return res
        # if all strings at index i are equal then that letter is added to result
        res += strs[0][i]
    return res
    
strs = ["bat","bag","bank","band"]
print(longestCommonPrefix(strs))