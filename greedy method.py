objects = [1, 2, 3, 4, 5, 6, 7]
profit = [10, 5, 15, 7, 6, 6, 18]
weight = [2, 3, 5, 7, 1, 4, 1]

n = 7
knapSackWeightMAXALLOWED = 15
PPU = []

for i in range(len(profit)):
    PPU.append((profit[i] / weight[i], profit[i], weight[i]))

PPU.sort(reverse=True, key=lambda x: x[0])
print(PPU)

maxprofit = 0
for crr in PPU:
    if knapSackWeightMAXALLOWED == 0:
        break
    CP, CW = crr[1], crr[2]
    print("Current item weight:", CW, "Current item profit:", CP)
    if CW <= knapSackWeightMAXALLOWED:
        knapSackWeightMAXALLOWED -= CW
        maxprofit += CP
        print(maxprofit, "<--- MAX Profit (after adding full item)")
    else:
        maxprofit += knapSackWeightMAXALLOWED * (CP / CW)
        knapSackWeightMAXALLOWED = 0
    print(knapSackWeightMAXALLOWED, "remaining weight allowed")
print("Total max profit:", maxprofit)
