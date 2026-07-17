class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = collections.defaultdict()
        dic['2'] = ['a','b','c']
        dic['3'] = ['d','e','f']
        dic['4'] = ['g','h','i']
        dic['5'] = ['j','k','l']
        dic['6'] = ['m','n','o']
        dic['7'] = ['p','q','r','s']
        dic['8'] = ['t','u','v']
        dic['9'] = ['w','x','y','z']

        #populate dic
        ans=[]
        res=[]

        def dfs(i):
            if i==len(digits):
                ans.append("".join(res))
                return

            for j in dic[digits[i]]:
                res.append(j)
                dfs(i+1)
                res.pop()
        dfs(0)    
        return ans
        