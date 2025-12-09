#O(n^2)
def KnapsackRec(w,vl,wt,n):

    if n==0 or w == 0:
        return 0
    pick = 0
    if wt[n-1] <= w:
        pick = vl[n-1] + KnapsackRec(w-wt[n-1],vl,wt,n-1)
    
    notPick = KnapsackRec(w,vl,wt,n-1)

    return max(pick,notPick)




def knapsack(w,vl,wt):
    
    n = len(vl)

    return KnapsackRec(w,vl,wt,n)

