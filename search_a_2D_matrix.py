from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Iterate through each row in the matrix
        for row in matrix:
            
            # Iterate through each element in the current row
            for value in row:
                
                # Check if the current element matches the target
                if value == target:
                    return True  # Target found
        
        # If the entire matrix is traversed and target is not found
        return False