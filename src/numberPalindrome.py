class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[::] == x[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    refSolution = Solution
    if(refSolution.isPalindrome(refSolution,121)):
        print('Palindrome')
    else:
        print('Not a palindrome')


