class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2 , len3 = len(s1), len(s2), len(s3)
        if len3 != len1 +len2:
            return False
        i1, i2, i3 = 0, 0, 0
        while i3<len(s3):
            if i2>=len(s2):
                if s3[i3:] == s1[i1:]:
                    return True
                else:
                    return False
            if i1>=len(s1):
                if s3[i3:] == s2[i2:]:
                    return True
                else:
                    return False

            if s3[i3]==s2[i2]:
                i3+=1
                i2+=1
            elif s3[i3]==s1[i1]:
                i3+=1
                i1+=1
            else:
                return False  
        return True        
        