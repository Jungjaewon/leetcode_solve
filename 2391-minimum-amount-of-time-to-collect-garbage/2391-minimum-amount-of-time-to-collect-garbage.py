class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = [0]
        def collect_gar(type_g):
            last_idx = -1
            for idx, cnt_dict in enumerate(garbage):
                if type_g in cnt_dict:
                    last_idx = idx
            if last_idx == -1:
                return
            else:
                for idx, s in enumerate(garbage):
                    if type_g in s:
                        new_s = s.replace(type_g, '')
                        ans[0] += len(s) - len(new_s)
                        garbage[idx] = new_s
                    
                    if last_idx == idx:
                        break
                    elif idx + 1 != len(garbage):
                        ans[0] += travel[idx]
        collect_gar('P')
        collect_gar('G')
        collect_gar('M')
        return ans[0]
        """
        from collections import Counter
        garbage, ans = [ dict(Counter(s)) for s in garbage], [0]
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
                        del cnt_dict[type_g]
                    
                    if idx == last_idx:
                        break
                    elif idx + 1 != len(garbage):
                        ans[0] += travel[idx]
                        #print('move : ', ans[0], idx)

        collect_gar('P')
        collect_gar('G')
        collect_gar('M')
        return ans[0]
        """
        