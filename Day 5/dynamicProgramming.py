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
            print(dp)
    return dp[1]