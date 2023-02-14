class Solution:
    def defangIPaddr(self, address: str) -> str:
        #return address.replace(".", "[.]")
        #return "[.]".join(address.split('.'))
        s = ''
        for c in address:
            if c.isdigit():
                s += c
            else:
                s += "[.]"
        return s