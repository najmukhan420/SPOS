blocksize = [100,500,200,300,600]
processsize = [212,417,112,250]
blocknum = [-1]*len(blocksize)
m = len(blocksize)
n = len(processsize)

for i in range(n):
    for j in range(m):
        maximum = max(blocksize)
        indexOfMax = blocksize.index(maximum)
        if blocksize[indexOfMax]>=processsize[i]:
            afterFit = blocksize[indexOfMax] - processsize[i]
            blocksize[indexOfMax] = afterFit
            blocknum[indexOfMax] = indexOfMax + 1
            break
        else:
            blocknum[j] = 'Not Allocated'
    print(i,'\t',processsize[i],'\t',blocknum[indexOfMax])
                