class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1={}
        f2={}
        if len(s)!=len(t):
            return False
        else:
            for char1 in s:
                if char1 in f1:
                    f1[char1]+=1
                else:
                    f1[char1]=1
            for char2 in t:
                if char2 in f2:
                    f2[char2]+=1
                else:
                    f2[char2]=1
            return f1==f2 
