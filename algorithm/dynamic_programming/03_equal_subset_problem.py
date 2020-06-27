# recursion
def equalSum(val):
    W=0
    n=len(val)
    for i in val:
        W += i
    if(W%2==0):
        return subsetSum(val,n-1,W//2)
    else:
        return False

def subsetSum(val,n,W):
    if(W==0):
        return True
    if(n<0):
        return False
    else:
        include = subsetSum(val,n-1,W-val[n])
        exclude = subsetSum(val,n-1,W)
        return include or exclude





val = [1,5,11,5]
result = equalSum(val)
print(result)