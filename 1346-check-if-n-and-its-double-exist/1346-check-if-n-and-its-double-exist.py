class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        a_dict = defaultdict(list)
        for i, n in enumerate(arr):
            a_dict[n].append(i)
        for i, n in enumerate(arr):
            key = int(n * 2)
            idx_list = a_dict[key]
            if key in a_dict and len(idx_list):
                for j in idx_list:
                    if i != j:
                        return True
        return False
                
                