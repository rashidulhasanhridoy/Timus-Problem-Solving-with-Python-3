N = int(input(''))
if N > 0:
    sum = N * (N + 1) // 2
else:
    sum = 1 + N * (1 - N) // 2
print(sum)