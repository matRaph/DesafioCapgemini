
def anagram_pair(s):
    out = 0
    for i in range(1,len(s)):
        d={}
        for j in range(len(s)-i+1):
            subarrays = ''.join(sorted(s[j:j+i]))
            if subarrays not in d:
                d[subarrays]=1
            else:
                d[subarrays]+=1
            
            out +=d[subarrays]-1
    return out
print(anagram_pair(input()))