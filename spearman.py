import numpy as np
import scipy.stats

# calculate the Spearman's coefficient for each graph

listOfBin = [x1,x2] # list that contains the individual data arrays
spearmanResults = []    # list that contains the Spearman Rho's coefficients & p-values
rhoResults = []     # list that contains only the Spearman Rho coefficients

for i in range(len(listOfBin)):

    result = scipy.stats.spearmanr(listOfBin[i],y)
    spearmanResults.append(result)

smallestDifference = abs(spearmanResults[0][0] - 1.0)
highestCoefficientIndex = 0   #index of the highest absolute value coefficient in spearmanResults[]

#find the index of the highest coefficient in the list
for i in range(1,len(spearmanResults)):
    currentDifference = abs(spearmanResults[i][0] - 1.0)

    if(currentDifference < smallestDifference):
        smallestDifference = currentDifference
        highestCoefficientIndex = i

#store only the Spearman Rho coefficients in its own list
for i in range(len(spearmanResults)):
    rhoResults.append(spearmanResults[i][0])

highest_spearman_register_name = [k for k,v in locals().items() if v is listOfBin[highestCoefficientIndex]][0]    # variable that contains the name of the bin that has the highest absolute Spearman's Rho Coefficient

print(spearmanResults)
print(rhoResults)
print(highest_spearman_register_name)


# rank each graph by their Spearman's coefficient

rankOfBinList = np.ndarray.tolist(scipy.stats.rankdata(rhoResults))    # list that stores the rank of the bins according to their Spearman Rho's coefficient (Note: lowest coefficient is '1')
print(rankOfBinList)



# Select the graph with the strongest correlation based on the Spearman's coefficient
highestRankIndex = rankOfBinList.index(2)
print(highestRankIndex)
