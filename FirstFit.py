blockSize = [300,50,200,350,70]
processSize = [200,47,212,426,10]
m = len(processSize)
n = len(blockSize)
blockNum = [-1]*n



for i in range(m):
    for j in range(n):
        if blockSize[j]>=processSize[i]:
            afterFit = blockSize[j]-processSize[i]
            blockSize[j]= afterFit
            blockNum[j]= j+1
            break
        if processSize[i]>blockSize[j]:
            blockNum[j]='not allocated'
    print(i,'\t',processSize[i],'\t',blockNum[j])