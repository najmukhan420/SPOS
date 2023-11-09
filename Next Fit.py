blocksize = [100,500,200,300,600]
processsize = [212,417,112,250]
blocknum = [-1]*len(blocksize)
m = len(blocksize)
n = len(processsize)
start = 0

for i in range(n):
    for j in range(start,m):
        if blocksize[j]>=processsize[i]:
         afterfit = blocksize[j] - processsize[i]
         blocksize[j] = afterfit
         blocknum[j] = j+1
         start = j+1
         if start==m:
             start = 0
         break
        else:
            blocknum[j] = 'Not Allocated'
    print(i,'\t',processsize[i],'\t',blocknum[j])
                