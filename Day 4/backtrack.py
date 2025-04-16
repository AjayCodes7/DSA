def permute(nums):
    #write code here   
    subsets = []
    def backtrack(n, subset):
        if n == len(nums):
            subsets.append(subset[:])
            return
        subset.append(nums[n])
        backtrack(n+1,subset)
        subset.pop()
        backtrack(n+1,subset)
    
    backtrack(0, [])
    return subsets
print(permute([]))

# def permute(nums):
#     result = set()
#     def swap(i,j):
#         nums[i], nums[j] = nums[j], nums[i]
#     def backtrack(n):
#         if n == len(nums):
#             result.add(nums[:])
#             return
#         for i in range(n, len(nums)):
#             swap(i,n)
#             backtrack(n+1)
#             swap(i,n)
#     backtrack(0)
#     return result
# print(permute([1,2,3]))
