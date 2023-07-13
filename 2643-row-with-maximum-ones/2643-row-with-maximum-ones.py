class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        """
        ans_idx, cnt = 0, -10e4
        for idx, row in enumerate(mat):
            one_cnt = row.count(1)
            if one_cnt > cnt:
                cnt = one_cnt
                ans_idx = idx   
        return [ans_idx, cnt]
        """
        """
        ans_idx, cnt = 0, -10e4
        for idx, row in enumerate(mat):
            one_cnt = sum(row)
            if one_cnt > cnt:
                cnt = one_cnt
                ans_idx = idx   
        return [ans_idx, cnt]
        """
        mat = [ [idx, sum(row)] for idx, row in enumerate(mat)]
        return sorted(mat, key=lambda x : (x[1], -x[0]))[-1]
            
            