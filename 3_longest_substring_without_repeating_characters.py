class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        fast_idx = 0
        max_len = 0
        char_set = set()
        
        for slow_idx in range(len(s)):
            while fast_idx < len(s) and s[fast_idx] not in char_set:
                char_set.add(s[fast_idx])
                max_len = max(max_len, len(char_set))
                fast_idx += 1
            char_set.remove(s[slow_idx])
        return max_len


if __name__ == '__main__':
    s = 'abcabcbb'
    ans = 3
    solution = Solution()
    my_ans = solution.lengthOfLongestSubstring(s)
    print(my_ans)
    assert my_ans == ans
