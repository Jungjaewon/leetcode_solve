class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        temp_set, temp_dict = set(), defaultdict(int)
        for edge in edges:
            temp_dict[edge[0]] +=1
            temp_dict[edge[1]] +=1
            for e in edge:
                temp_set.add(e)
        #ans = [[e, c] for e, c in temp_dict.items()]
        return sorted([[e, c] for e, c in temp_dict.items()],key=lambda x:-x[1])[0][0]
        
        