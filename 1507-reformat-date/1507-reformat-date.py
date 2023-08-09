class Solution:
    def reformatDate(self, date: str) -> str:
        d, m, y = date.split(' ')
        m_dict = {'Jan' : 1, 'Feb': 2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
        return f'{y}-{str(m_dict[m]).zfill(2)}-{str(d[:-2]).zfill(2)}'