def subsets(nums):
    """Generates all subsets of the given array"""
    result = []
    def backtrack(n, subset):
        if n == len(nums):
            result.append(subset[:])
            return
        subset.append(nums[n])
        backtrack(n+1,subset)
        subset.pop()
        backtrack(n+1,subset)
    
    backtrack(0, [])
    return result
# print(subsets([1,2,3]))

def permute(nums):
    """All permutations of the given array/List"""
    result = set()
    def swap(i,j):
        nums[i], nums[j] = nums[j], nums[i]

    def backtrack(n):
        if n == len(nums):
            result.add(nums[:])
            return
        for i in range(n, len(nums)):
            swap(i,n)
            backtrack(n+1)
            swap(i,n)
    backtrack(0)
    return result
# print(permute([1,2,3]))

def combine(n,k):
    """
    Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
    You may return the answer in any order.
    """
    result = []
    def backtrack(i,combination):
        if len(combination) == k:
            result.append(combination[:])
            return
        if i > n or len(combination) > k:
            return
        # Include
        combination.append(i)
        backtrack(i+1,combination)
        # Exclude
        combination.pop()
        backtrack(i+1,combination)
    backtrack(1,[])
    return result
# print(combine(4,2))

def combinationSum1(candidates, target):
    """
    Given an array of distinct integers candidates and a target integer target, 
    return a list of all unique combinations of candidates where the chosen numbers 
    sum to target. You may return the combinations in any order.The same number may 
    be chosen from candidates an unlimited number of times. Two combinations are unique 
    if the frequency of at least one of the chosen numbers is different.
    (the integers in the candidates array are all non negative )
    """
    # Using for loop
    result =[]
    def backtrack(n, candidate, currSum):
        if target == currSum:
            result.append(candidate[:])
            return
        for i in range(n, len(candidates)):
            if currSum + candidates[i] <= target:
                candidate.append(candidates[i])
                backtrack(i,candidate,currSum+candidates[i])
                candidate.pop()
    backtrack(0,[],0)
    return result
# print(combinationSum1([2,3,8,9],9))

def combinationSum2(candidates, target):
    """
    Given a collection of candidate numbers (candidates) and a target number (target),
    find all unique combinations in candidates where the candidate numbers sum to target.
    Each number in candidates may only be used once in the combination.
    Note: The solution set must not contain duplicate combinations.
    """
    # Without for loop
    result =[]
    def backtrack(n, candidate, currSum):
        if target == currSum:
            result.append(candidate[:])
            return
        if n == len(candidates):
            return
        if currSum + candidates[n] <= target:
            candidate.append(candidates[n])
            backtrack(n,candidate,currSum+candidates[n])
            candidate.pop()
        backtrack(n+1,candidate, currSum)
    backtrack(0,[],0)
    return result
# print(combinationSum2([2,3,8,9],9))

def combinationSum3(candidates, target):
    candidates.sort()
    result =[]
    def backtrack(n, candidate, currSum):
        if target == currSum:
            if candidate not in result:
                result.append(candidate[:])
                return
        if n == len(candidates):
            return
        if currSum > target:
            return
        hash = set()
        for i in range(n,len(candidates)):
            if candidates[i] not in hash:
                hash.add(candidates[i])
                candidate.append(candidates[i])
                backtrack(i+1,candidate,currSum+candidates[i])
                candidate.pop()
    backtrack(0,[],0)
    return result
# print(combinationSum3([3,3,3,6,9],9))


def combinationSum4(k, n):
    """
    Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    Only numbers 1 through 9 are used.
    Each number is used at most once.
    Return a list of all possible valid combinations. The list must not contain the same combination twice, 
    and the combinations may be returned in any order.
    """
    result = []
    def backtrack(i,combination, currSum):
        #Base Case 
        if currSum == n and len(combination) == k:
            result.append(combination[:])
            return
        if i > 9 or currSum >= n or len(combination) == k:
            return
        # Include
        combination.append(i)
        backtrack(i+1,combination, currSum + i)
        # Exclude
        combination.pop()
        backtrack(i+1,combination, currSum)
    backtrack(1,[],0)
    return result

# print(combinationSum4(k=3, n=24))


def solveSudoku(board):
    #The function modifies the board in place to present the solution .Hence there is no need to return the board
    def valid_numbers(i, j):
        # Valid numbers W.R.T Rows
        nums = [str(n) for n in range(1,10) if str(n) not in board[i]]
        # Valid numbers W.R.T Cols
        for k in range(0,9):
            if board[k][j] in nums:
                nums.remove(board[k][j])
        # Valid numbers W.R.T current Grid
        g_i, g_j = i//3*3,j//3*3
        for a in range(g_i, g_i+3):
            for b in range(g_j, g_j+3):
                if board[a][b] in nums:
                    nums.remove(board[a][b])
        return nums
    def is_valid(i, j, n):
        # Rows and Cols
        for k in range(0,9):
            if board[k][j] == n or board[i][k] == n:
                return False
        # 3X3 Grid
        g_i, g_j = i//3*3,j//3*3
        for a in range(g_i, g_i+3):
            for b in range(g_j, g_j+3):
                if board[a][b] == n:
                    return False
        return True

    def backtrack():
        for a in range(9):
            for b in range(9):
                if board[a][b] == ".":
                    for option in range(1,10):
                        if is_valid(a,b,str(option)):
                            board[a][b] = str(option)
                            if backtrack():
                                return True
                            board[a][b] = "."
                    return False
        return True
    backtrack()
    print(board)

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
# solveSudoku(board)

def solveSudoku2(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty = []

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                empty.append((i, j))
            else:
                rows[i].add(val)
                cols[j].add(val)
                boxes[(i // 3) * 3 + (j // 3)].add(val)

    def backtrack(index):
        if index == len(empty):
            return True
        i, j = empty[index]
        box_id = (i // 3) * 3 + (j // 3)
        for num in '123456789':
            if num not in rows[i] and num not in cols[j] and num not in boxes[box_id]:
                board[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_id].add(num)
                if backtrack(index + 1):
                    return True
                # Backtrack
                board[i][j] = "."
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[box_id].remove(num)
        return False
    backtrack(0)
    print(board)

# solveSudoku2(board)

def solveNQueens(n):
    #write code here
    cols = set()
    posDiag = set()
    negDiag = set()

    board = [['.']*n for _ in range(n)]
    result = []
    def backtrack(r):
        if r == n:
            result.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c not in cols and (r+c) not in posDiag and (r-c) not in negDiag:
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
    backtrack(0)
    return result
print(solveNQueens(4))