X = str(input(''))
count = 0
for i in X:
    if i == ' ':
        break
    count += 1
M = str(X[0 : count])
N = int(M)
K = len(X[count + 1:])
sum = 1
for i in range(N, 0, -K):
    sum *= i
print(sum)