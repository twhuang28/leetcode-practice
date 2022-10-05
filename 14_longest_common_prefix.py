
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        test_prefix = ""
        prefix = ""
        for char in strs[0]:
            test_prefix += char
            count = 0
            for word in strs:
                if not word.startswith(test_prefix):
                    break
                else:
                    count += 1
            if count == len(strs):
                prefix = test_prefix
            else:
                return prefix
        return prefix


if __name__ == '__main__':
    s = ["flower","flow","flight"]
    ans = "fl"
    solution = Solution()
    my_ans = solution.longestCommonPrefix(s)
    print(my_ans)
    assert my_ans == ans