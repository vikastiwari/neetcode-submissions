class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len1 = len(s1)
        len2 = len(s2)

        if(len2<len1):
            return False

        dict_1 = {}
        dict_2 = {}

        for index,ch in enumerate(s1):
            dict_1[ch] = dict_1.get(ch,0) + 1
            dict_2[s2[index]] = dict_2.get(s2[index],0) + 1

        if dict_1 == dict_2:
                return True

        
        left = 0
        right =  len1

        while right<len2:

            dict_2[s2[right]] = dict_2.get(s2[right],0) + 1
            dict_2[s2[left]]=dict_2[s2[left]]-1

            if dict_2[s2[left]]==0:
                del dict_2[s2[left]]  

            left+=1
            right+=1


            if dict_1 == dict_2:
                return True
                
        return False
        