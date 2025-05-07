L = [7,4,3,12,8]
temp = 0

for i in range(len(L)):

    for j in range(len(L) - 1):

        if L[j] < L[j + 1]:

            temp = L[j]
            L[j] = L[j + 1]
            L[j + 1] = temp

print(L)