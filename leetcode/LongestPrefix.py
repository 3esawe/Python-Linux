def longestCommonPrefix (strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        rstr = ""
        for i in strs:
            for j in i:
                if j in i:
                    rstr += j
        return rstr
if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
