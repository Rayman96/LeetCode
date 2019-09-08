class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A_square = []
        for x in A:
            A_square.append(x*x)
        ans =sorted(A_square,reverse=False)
        return ans