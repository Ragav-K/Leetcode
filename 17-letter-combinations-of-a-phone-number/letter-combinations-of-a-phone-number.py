class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        letters = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        ans = []

        def rec(index,current):
            if index == len(digits):
                ans.append(current)
                return
            for ch in letters[digits[index]]:
                rec(index+1,current+ch)

        rec(0,"")
        return ans