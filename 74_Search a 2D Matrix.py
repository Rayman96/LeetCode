class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        
        import numpy as np
        new_matrix = list(list(np.array(matrix).reshape(1, -1))[0])
        low, high = 0, len(new_matrix)-1
        
        while low <= high:
            mid = int((low+high)/2)
            
            if target == new_matrix[mid] or target == new_matrix[low] or target == new_matrix[high]:
                return True
            else:
                if new_matrix[low] < target < new_matrix[mid]:
                    high = mid -1
                else:
                    low = mid +1
                    
        return False