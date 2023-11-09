blocksize = [100,500,200,300,600]
blocksizesorted = [100,500,200,300,600]
processsize = [212,417,112,250]
blocknum = [-1]*len(blocksize)
m = len(blocksize)
n = len(processsize)

for i in range(n):
    for j in range(m):
        blocksizesorted.sort()
        if blocksizesorted[j]>=processsize[i]:
            bestblock = blocksizesorted[j]
            indexofblock = blocksize.index(bestblock)
            blocknum[indexofblock] = indexofblock+1
            afterfit = blocksizesorted[j]-processsize[i]
            blocksizesorted[j]=afterfit
            blocksize[indexofblock]=afterfit
            break
        else:
            blocknum[j] = 'Not Allocated'
    print(i,'\t',processsize[i],'\t',blocknum[indexofblock])
                