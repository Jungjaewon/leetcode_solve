class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        from collections import Counter
        garbage, ans = [ dict(Counter(s)) for s in garbage], [0]
        #print(garbage)
        def collect_gar(type_g):
            last_idx = -1
            for idx, cnt_dict in enumerate(garbage):
                if type_g in cnt_dict:
                    last_idx = idx
            if last_idx == -1:
                return
            else:
                for idx, cnt_dict in enumerate(garbage):
                    if type_g in cnt_dict:
                        ans[0] += cnt_dict[type_g]
                        #print('collect : ', ans[0], idx)
                        del cnt_dict[type_g]
                    
                    if idx == last_idx:
                        break
                    elif idx + 1 != len(garbage):
                        ans[0] += travel[idx]
                        #print('move : ', ans[0], idx)

        collect_gar('P')
        #print(ans[0])
        collect_gar('G')
        #print(ans[0])
        collect_gar('M')
        #print(ans[0])
        return ans[0]
        