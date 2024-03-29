class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        a, b = s[:len(s) // 2], s[len(s) // 2:]
        a_sum = sum([a.count(c) for c in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']])
        b_sum = sum([b.count(c) for c in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']])
        return a_sum == b_sum
        """
        """
        a_sum = sum([s[:len(s) // 2].count(c) for c in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']])
        b_sum = sum([s[len(s) // 2:].count(c) for c in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']])
        return a_sum == b_sum
        """
        """
        return sum([s[:len(s) // 2].count(c) for c in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']]) == sum([s[len(s) // 2:].count(c) for c in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']])
        """
        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        return sum([s[:len(s) // 2].count(c) for c in vowels]) == sum([s[len(s) // 2:].count(c) for c in vowels])