# https://leetcode.com/problems/add-binary/

import unittest

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        maxLength = max(len(a), len(b))
        
        reverseAList = list(a.zfill(maxLength)[::-1])
        reverseBList = list(b.zfill(maxLength)[::-1])
        
        answer = ""
        increment = 0

        for i in range(maxLength):
            sum = increment + int(reverseAList[i]) + int(reverseBList[i])
            answer += str(sum % 2)
            increment = sum // 2
        
        while (increment > 0):
            answer += str(increment % 2)
            increment //= 2
        
        return answer[::-1]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_case_1(self):
        self.assertEqual(self.solution.addBinary("11", "1"), "100")
    
    def test_case_2(self):
        self.assertEqual( \
            self.solution.addBinary( \
                "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101", \
                "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"), \
            "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000")

if __name__ == '__main__':
    unittest.main()
