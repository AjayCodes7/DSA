class recursion:
    def __init__(self):
        pass

    def factorial(self, n):
        if n <= 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def genPattern(self, n):
        """
        n = 1 -> 11
        n = 2 -> 2112
        n = 3 -> 321123
        and so on 
        """
        if n == 0:
            return
        print(n,end=" ")
        self.genPattern(n-1)
        print(n, end=" ")

    def sumOfFirstN(self,n):
        """
        Sum of First N natural numbers
        """
        if n < 0:
            return 0
        return n + self.sumOfFirstN(n-1)

    def sumUptoN(self,curr, n):
        """
        Sum of First N natural numbers
        """
        if curr == n:
            return n
        return curr + self.sumUptoN(curr+1,n)


    def kth_symbol(self,n, k):
        """
        Problem:
            (Leetcode: 779): We build a table of n rows (1-indexed). We start by writing 0 
            in the 1st row. Now in every subsequent row, we look at the previous row and replace each
            occurrence of 0 with 01, and each occurrence of 1 with 10. For example, for n = 3, the 1st
            row is 0, the 2nd row is 01, and the 3rd row is 0110. Given two integer n and k, return the
            kth (1-indexed) symbol in the nth row of a table of n rows.
        """
        if n == 1:
            return 0
        half = 2**(n-1)//2
        if k <= half:
            return self.kth_symbol(n-1,k)
        else:
            return int(not(self.kth_symbol(n-1, k-half)))
    def Josephus(self,n,k):
        def recurse(nums,c,k):
            if len(nums) == 1:
                return nums[0]
            c = (c+k-1) % len(nums)
            nums.pop(c)
            return recurse(nums,c,k)
        return recurse([i for i in range(1,n+1)],0, k)


obj = recursion()
obj.genPattern(3)
print(obj.sumOfFirstN(10))
print(obj.sumUptoN(0,10))