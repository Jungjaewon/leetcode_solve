class Solution:
    def reformatDate(self, date: str) -> str:
        """
        d, m, y = date.split(' ')
        m_dict = {'Jan' : 1, 'Feb': 2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
        return f'{y}-{str(m_dict[m]).zfill(2)}-{str(d[:-2]).zfill(2)}'
        """
        d, m, y = date.split(' ')
        m_dict = {'Jan' : '01', 'Feb': '02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        return f'{y}-{m_dict[m]}-{str(d[:-2]).zfill(2)}'