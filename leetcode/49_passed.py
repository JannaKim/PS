class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for idx, word in enumerate(strs):
            ths = list(word)
            ths.sort()
            ths = ''.join(ths)
            if ths not in dic:
                dic[ths] = []
            dic[ths].append(idx)
        ans = []
        for v in dic.values():
            tmp = []
            for num in v:
                tmp.append(strs[num])
            ans.append(tmp)
        return ans

'''
Runtime: 96 ms, faster than 77.50% of Python3 online submissions for Group Anagrams.
Memory Usage: 18.5 MB, less than 24.96% of Python3 online submissions for Group Anagrams.

'''