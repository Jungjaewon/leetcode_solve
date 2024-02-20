class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        k = len(grid[0])
        n_list, check_dict = list(), dict()
        twice = -1
        for line in grid:
            n_list.extend(line)
        for n in n_list:
            if n in check_dict:
                twice = n
                break
            else:
                check_dict[n] = 1
        print(set(range(1, k**2 + 1)))
        print(list(set(range(1, k**2 + 1)) - set(n_list)))
        miss = list(set(range(1, k**2 + 1)) - set(n_list))[0]
        return [twice, miss]
            
        
        