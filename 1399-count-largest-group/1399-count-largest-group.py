class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        a_dict = defaultdict(list)
        for i in list(range(1, n + 1)):
            a_dict[sum([int(c) for c in str(i)])].append(i)
        a_list = [len(x) for x in sorted(list(a_dict.values()), key=lambda x : len(x))]
        return Counter(a_list)[max(a_list)]
        """
        """
        a_dict = defaultdict(list)
        for i in list(range(1, n + 1)):
            a_dict[sum([int(c) for c in str(i)])].append(i)
        a_list = [len(x) for x in a_dict.values()]
        return Counter(a_list)[max(a_list)]
        """
        a_dict, large_c = defaultdict(list), 0
        for i in list(range(1, n + 1)):
            key = sum([int(c) for c in str(i)])
            a_dict[key].append(i)
            large_c = max(large_c, len(a_dict[key]))
        return len([1 for key in a_dict if len(a_dict[key]) == large_c])
        
        
        
        