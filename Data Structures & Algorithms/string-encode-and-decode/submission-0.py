class Solution:

    def encode(self, strs: List[str]) -> str:
        answer=""
        for s in strs:
            answer+=str(len(s))+"#"+s
        return answer    

    def decode(self, s: str) -> List[str]:
        answer=[]
        i=0

        while i<len(s):
            j=i

            while s[j]!='#':
                j+=1

            number = int(s[i:j])

            start=j+1
            end=start+number

            answer.append(s[start:end])

            i=end    



        return answer