def longestCommonPrefix (strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        dumpdict = {}
        rstr = ""
        for i in strs[0]:
            dumpdict[i] = dumpdict.get(i, 0) + 1
        for i in strs[1:len(strs)]:
            for j in i:
                dumpdict[j] = dumpdict.get(j, 0) +1
        key_max = max(dumpdict.keys(), key=(lambda k: dumpdict[k]))
        val = dumpdict[key_max]
        if val == 1:
            return rstr
        else:
            for i, v in dumpdict.items():
                if v == val:
                    rstr += i
            return rst

def longestCommonPrefix1(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
