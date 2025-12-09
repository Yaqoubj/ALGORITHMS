def knapsackRec(w,vl,wt,n,memo):
    
    if n == 0 or w == 0:
        return 0 
    if memo[n][w] != -1:
        return memo[n][w]    
    pick = 0

    if wt[n-1] <= w:
        pick = vl[n-1] + knapsackRec(w-wt[n-1],vl,wt,n-1,memo)

    notpick = knapsackRec(w,vl,wt,n-1,memo)

    memo[n][w] = max(pick,notpick)
    return memo[n][w]
    
    #2d list, loop will create n lists and assign them to memo
def knapsack(w,vl,wt):
    n =len(wt)
    memo =[[-1]*(w+1) for _ in range(n+1)]
    return knapsackRec(w,vl,wt,n,memo)

w = 5
val = [1,2,3]
wt = [3,2,1]
print(knapsack(w,val,wt))