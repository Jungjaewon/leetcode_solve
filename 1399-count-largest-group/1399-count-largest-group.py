class Solution:
    def countLargestGroup(self, n: int) -> int:
        a_dict = defaultdict(list)
        for i in list(range(1, n + 1)):
            a_dict[sum([int(c) for c in str(i)])].append(i)
        a_list = [len(x) for x in sorted(list(a_dict.values()), key=lambda x : len(x))]
        return Counter(a_list)[max(a_list)]
        
        
        
        