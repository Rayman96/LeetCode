class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import numpy as np 
        matrix = list(list(np.array(matrix).reshape(1, -1))[0])
        
        matrix = np.sort(matrix)
        
        return matrix[k-1]