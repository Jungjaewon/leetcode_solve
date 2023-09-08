class Solution:
    def average(self, salary: List[int]) -> float:
        #return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
        salary = sorted(salary)
        return (sum(salary) - salary[0] - salary[-1]) / (len(salary) - 2)