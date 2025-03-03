
#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

#Example 1:

#Input: strs = ["flower","flow","flight"]
#Output: "fl"

#Example 2:

#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.

def longest_common_prefix(strs : list[str]) -> str:
    common_prefix = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return common_prefix
        common_prefix += first[i]

    return common_prefix


print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["dog","racecar","car"]))