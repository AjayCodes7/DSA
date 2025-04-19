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
            (Leetcode: 779): We build a table of n rows (1-indexed). We start by
            writing 0 in the 1st row. Now in every subsequent row, we look at the
            previous row and replace each occurrence of 0 with 01, and each 
            occurrence of 1 with 10. For example, for n = 3, the 1st row is 0, the
            2nd row is 01, and the 3rd row is 0110. Given two integer n and k, return
            the kth (1-indexed) symbol in the nth row of a table of n rows.
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
    
    def power_sum(self,array,power=1):
        """
        Power Sum - Let's define a peculiar type of array in which each element 
        is either an integer or another peculiar array. Assume that a peculiar 
        array is never empty. Write a function that will take a peculiar array 
        as its input and find the sum of its elements. If an array is an element 
        in the peculiar array you have to convert it to it's equivalent value so 
        that you can sum it with the other elements. Equivalent value of an array 
        is the sum of its elements raised to the number which represents how far 
        nested it is. For e.g. [2,3[4,1,2]] = 2+3+ (4+1+2)^2
        """
        def recurse(n, power=1):
            if n == len(array):
                return 0
            if type(array[n]) == list:
                return self.power_sum(array[n],power+1)**(power+1) + recurse(n+1,power)
            return array[n] + recurse(n+1,power)
        return recurse(0, power)


obj = recursion()
# obj.genPattern(3)
# print(obj.sumOfFirstN(10))
# print(obj.sumUptoN(0,10))
print(obj.power_sum([1,2,[7,[3,4],2]]))