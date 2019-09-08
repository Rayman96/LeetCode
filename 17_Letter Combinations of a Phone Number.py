class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'1':[],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'], '8':['t','u','v'],'9':['w','x','y','z'],'0':[]}
        output = []
        if not digits:
            return []
        if len(digits) == 1:
            return dict[digits]
        listA = self.letterCombinations(digits[0:-1])
        listB = dict[digits[-1]]
        return [f'{i}{j}' for i in listA for j in listB]