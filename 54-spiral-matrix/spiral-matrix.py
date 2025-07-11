class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        res = []
        while left<right+1 and top<bottom+1:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top +=1
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -=1

            if not (left<right+1 and top<bottom+1):
                break
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -=1
            for i in range(bottom,top-1, -1):
                res.append(matrix[i][left])
            left +=1
        return res


        