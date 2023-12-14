class Solution:
    def countTime(self, time: str) -> int:
        t, m = time.split(":")
        if t == '??':
            t_n = 24
        elif t[0] != '?' and t[1] == '?':
            if t[0] == '0' or t[0] == '1':
                t_n = 10
            else:
                t_n = 4
        elif  t[0] == '?' and t[1] != '?':
            if int(t[1]) < 4: 
                t_n = 3
            else:
                t_n = 2
        elif  t[0] != '?' and t[1] != '?':
            t_n = 1
            
        if m == '??':
            m_n = 60
        elif m[0] != '?' and m[1] == '?':
            m_n = 10
        elif m[0] == '?' and m[1] != '?':
            m_n = 6
        elif m[0] != '?' and m[1] != '?':
            m_n = 1
        
        return t_n * m_n
            
        
        