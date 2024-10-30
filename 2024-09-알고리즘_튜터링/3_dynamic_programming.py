# 피보나치 수열을 동적 계획법으로 구현 (메모이제이션)
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# 피보나치 수열 계산 예시
n = 10
print(f"Fibonacci({n}) =", fibonacci(n))

# 두 문자열의 최장 공통 부분 수열 (LCS) 찾기
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    # 동적 계획법 테이블 생성
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

# 두 문자열의 LCS 길이 구하기 예시
X = "AGGTAB"
Y = "GXTXAYB"
print(f"LCS length: {lcs(X, Y)}")

# 배낭 문제 - 동적 계획법
def knapsack(W, wt, val, n):
    # 동적 계획법 테이블 생성
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][W]

# 배낭 문제 예시
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(f"Maximum value in Knapsack: {knapsack(W, wt, val, n)}")
