class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_list = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        integer_list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        answer = ''
        
        for idx in range(len(roman_list)):
            answer += ( num // integer_list[idx] ) * roman_list[idx]
            num = num % integer_list[idx]

        return answer


if __name__ == '__main__':
    s = 58
    ans = 'LVIII'
    solution = Solution()
    my_ans = solution.intToRoman(s)
    print(my_ans)
    assert my_ans == ans
