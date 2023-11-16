class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local_name, domain = email.split('@')
            local_name = local_name.replace('.', '')
            if '+' in local_name: 
                p_idx = local_name.find('+')
                local_name = local_name[:p_idx]
            ans.add(f'{local_name}@{domain}')
        print(ans)
        return len(ans)