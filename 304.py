class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0] * n for _ in range(m)]
        
        self.dp[0][0] = matrix[0][0]
        for i in range(1, m):
            self.dp[i][0] = self.dp[i-1][0] + matrix[i][0]
        for j in range(1, n):
            self.dp[0][j] = self.dp[0][j-1] + matrix[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.dp:
            return 0
        
        top_left = self.dp[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        top_right = self.dp[row1-1][col2] if row1 > 0 else 0
        bottom_left = self.dp[row2][col1-1] if col1 > 0 else 0
        bottom_right = self.dp[row2][col2]
        
        return bottom_right - top_right - bottom_left + top_left
