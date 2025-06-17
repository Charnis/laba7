m = ["asdasdh", "aasds", "ahdas"]
b = 0
for i in range(len(m)):
    K = list(m[i])
    b += len(K)
print(f"Сумма длин всех строк: {b}")
