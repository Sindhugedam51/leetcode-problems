''' Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''



def longestcommonprefix(strs):
    pref=strs[0]
    x=len(pref)
    for i in strs[1:]:
        while pref!=i[0:x]:
            x-=1
            if x==0:
                return ""
            else:
                pref=pref[0:x]
    return pref
strs=["flower","flow","flight"]
print(longestcommonprefix(strs))

















