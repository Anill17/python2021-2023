class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bin1(y):
            left,right=0,len(matrix[0])
            while(left<right):
                mid=(left+right)//2
                if(matrix[y][mid]==target):
                    return True
                elif(matrix[y][mid]>target):
                    right=mid
                elif(matrix[y][mid]<target):
                    left=mid+1
                
            return False    
        
        def bin2(left_ver,right_ver):
            while(left_ver<right_ver):
                mid=(left_ver+right_ver)//2
                if(matrix[mid][0]<=target<=matrix[mid][-1]):
                    return bin1(mid)
                elif(matrix[mid][0]>target):
                    right_ver=mid
                elif(matrix[mid][-1]<target):
                    left_ver = mid+1
            return False    
                
            
            
        return bin2(0,len(matrix)) 