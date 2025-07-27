'''
BOTTOM UP APPROACH
'''
'''
def maxCommonStr(s1,s2):
    m=len(s1)
    n=len(s2)
    LCSuf=[[0]*(n+1)for _ in range(m+1)]
    res=0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1]== s2[j-1]:
                LCSuf[i][j]=LCSuf[i-1][j-1]+1
                res=max(res,LCSuf[i][j])
            else:
                LCSuf[i][j]=0
    return res
s1="xyzabcd"
s2="abcdxyz"
print(maxCommonStr(s1,s2))
'''

''' space optimized'''
'''
def longestCommonSubstr(s1,s2):
    m=len(s1)
    n=len(s2)
    prev=[0]*(n+1)
    res=0
    for i in range(1,m+1):
        curr=[0]*(n+1)
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                curr[j]=prev[j-1]+1
                res=max(res,curr[j])
            else:
                curr[j]=0
        prev=curr
    return res
s1="abcdxyz"
s2="xyzabcd"
print(longestCommonSubstr(s1,s2))
'''