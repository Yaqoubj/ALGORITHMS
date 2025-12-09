def kanpsack(w,vl,wt):
    n = len(wt)
    dp =[[0 for _ in range(w+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(w+1):

            if i == 0 or  j == 0:
                 dp[i][j] = 0
            else:
                pick = 0
            
            if wt[i-1] <= j:
                pick = vl[i-1] + dp[i-1][j-wt[i-1]]
                
            notPick = dp[i-1][j]
            
            dp[i][j] = max(pick,notPick)

        
    return dp[n][w]