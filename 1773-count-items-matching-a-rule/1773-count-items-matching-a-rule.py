class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx_dict = {'type': 0, 'color' : 1, 'name': 2}
        return len([item for item in items if ruleValue == item[idx_dict[ruleKey]]])