def fibonacci(n):
    #write code here
    dp = [0,1]
    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    else:
        for _ in range(n-1):
            dp[0],dp[1] = dp[1],dp[0] + dp[1]
    return dp[1]

def knapSack(w:int, wt:list, val:list, n:int):
    result = -1
    dp = [[-1]*(w+1) for _ in range(n+1)]
    def recurse(N, W):
        if N == n or W == 0:
            return 0
    
        if dp[N][W] != -1:
            return dp[N][W]
    
        if wt[N] > W:
            dp[N][W] = recurse(N + 1, W)
        else:
            include = val[N] + recurse(N + 1, W - wt[N])
            exclude = recurse(N + 1, W)
            dp[N][W] = max(include, exclude)
        return dp[N][W]
    return recurse(0, w)
# print(knapSack(5,[5, 4, 2, 3] ,[10, 40, 30, 50],4))


def knapSack(w:int, wt:list, val:list):
    dp = [[0]*(w+1) for _ in range(2)]
    for i in range(len(wt)):
        for j in range(w+1):
            if wt[i] > j:
                dp[1][j] = dp[0][j]
            else:
                dp[1][j] = max(dp[0][j], val[i] + (dp[0][j-wt[i]]))
        dp[0] = dp[1][:]
    return dp[-1][-1]
# print(knapSack(50,[10, 20, 30] ,[60, 100, 120]))

def knapSack(w, wt, val):
    dp = [[0]*(w+1) for _ in wt]
    for i in range(len(wt)):
        for j in range(w+1):
            if wt[i] > j:
                dp[i][j] = dp[i-1][j] if i > 0 else 0
            else:
                dp[i][j] = max(dp[i-1][j], val[i] + (dp[i-1][j-wt[i]] if i > 0 else 0))
    return dp[-1][-1] if dp else 0

# print(knapSack(50,[10, 20, 30] ,[60, 100, 120]))

def knapSack(N, W, val, wt):
    # iterative
    value = []
    for i in range(N):
        value.append([val[i],wt[i],round(val[i]/wt[i],2)])
        value.sort(key=lambda a: a[2], reverse=True)
    result = 0
    for value, weight, _ in value:
        while weight <= W:
            result += value
            W -= weight
    return result
# print(knapSack(2, 3, [4, 2], [3, 1]))

def knapSack(N, W, val, wt):
    # dynamic programming
    dp = [[0]*(W+1) for _ in range(N+1)]
    for item in range(1,N+1):
        for weight in range(1,W+1):
            if weight >= wt[item-1]:
                dp[item][weight] = max(dp[item-1][weight],val[item-1] + dp[item][weight-wt[item-1]])
            else:
                dp[item][weight] = dp[item-1][weight]
    return dp[-1][-1]
# print(knapSack(2, 3, [4, 2], [3, 1]))


def countSubstrings(s):
    # brute-force
    result = 0
    def recurse(n,sub):
        nonlocal result
        if sub and sub == sub[::-1]:
            result += 1
        if n == len(s):
            return 0
        recurse(n+1, sub+s[n])
        return result 
    for i in range(len(s)):
        recurse(i,"")
    return result

def countSubstrings(s):
    n = len(s)
    dp = [[-1]*n for _ in range(n)]
    def recurse(i,j):
        if i == j: 
            dp[i][j] = True
            return dp[i][j] 
        if dp[i][j] != -1:
            return dp[i][j]
        recurse(i, j-1)
        recurse(i+1, j)
        if s[i] == s[j] and (i+1 == j or recurse(i+1,j-1)):
            dp[i][j] = True
        else:
            dp[i][j] = False
    recurse(0,n-1)
    result = 0
    for d in range(n):
        print(dp[d])
        for i in range(0,n-d):
            j = d + i
            if dp[i][j]:
                result += 1
    return result

print(countSubstrings("gayii"))
