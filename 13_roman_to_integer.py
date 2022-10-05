class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {'I':1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result_int = 0
        for idx, char in enumerate(s):
            if idx != len(s) - 1 and roman_to_int[s[idx]] < roman_to_int[s[idx + 1]]:
                result_int += roman_to_int[char] * -1
            else:
                result_int += roman_to_int[char]
        return result_int


if __name__ == '__main__':
    s = 'LVIII'
    ans = 58
    solution = Solution()
    my_ans = solution.romanToInt(s)
    print(my_ans)
    assert my_ans == ans
