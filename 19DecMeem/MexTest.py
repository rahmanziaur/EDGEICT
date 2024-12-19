def mex(arr, N):
    arr.sort()
    mex = 0
    for idx in range(N):
        if arr[idx] == mex:
            mex += 1
    return mex
 
if __name__ == '__main__':
    arr = [1, 0, 2, 4]
    N = len(arr)
    print(mex(arr, N))