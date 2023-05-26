class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def check_devider(astr, divider):
            i = 0
            while i < len(astr):
                splice = astr[i:i+len(divider)]
                if splice != divider:
                    return False
                i += len(divider)
            return True
            
        divider = sorted([str1, str2], key=len)[0]
        i = len(divider)
        while i > 0:
            divider = divider[:i]
            i -= 1
            # fast check
            if len(str1) % len(divider) or len(str2) % len(divider):
                continue
            if not check_devider(str1, divider):
                continue
            if not check_devider(str2, divider):
                continue
            return divider
        return ""

