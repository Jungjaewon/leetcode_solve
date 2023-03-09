class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """        
        ans_dict = {a : b for a,b in paths}
        city_set = {b for a,b in paths}
        for city in city_set:
            if city not in ans_dict:
                return city
        """
        ans_dict = {a : b for a,b in paths}
        for A, B in ans_dict.items():
            if B not in ans_dict:
                return B
        
        
        