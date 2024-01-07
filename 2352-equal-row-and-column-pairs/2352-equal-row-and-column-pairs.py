class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        #col_list = list(zip(*grid))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                temp_list1, temp_list2 = [], []
                
                for k in range(len(grid[i])):
                    temp_list1.append(grid[i][k])
                    
                for k in range(len(grid[i])):
                    temp_list2.append(grid[k][j])
                #print(temp_list1, temp_list2)
                if temp_list1 == temp_list2:
                    ans += 1
        return ans