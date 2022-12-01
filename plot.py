import matplotlib.pyplot as plt

#PIONEER
minsup = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]
zt = [1924.40625, 700.234375, 299.828125, 121.5625, 52.3125, 26.4375, 10.96875]
rvt = [1192.015625, 417.84375, 176.109375, 72.03125, 33.046875, 15.96875, 6.96875]

plt.subplot(1, 3, 1)
plt.plot(minsup, zt, label = "Z-Miner", marker = 'o')
plt.plot(minsup, rvt, label = "Z-Miner_RV", marker = 's')
plt.title("PIONEER (max k = 14, Speedup ≈ 1.7)")
plt.xlabel("Minimum Support")
plt.ylabel("Time (Seconds)")
plt.legend()
#plt.yscale("log")

#CONTEXT
minsup = [0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98]
zt = [1475.1875, 942.484375, 673.90625, 432.828125, 96.265625, 40.78125, 19.078125]
rvt = [1024.28125, 605.8125, 436.296875, 297.328125, 70.53125, 28.796875, 15.0]

plt.subplot(1, 3, 2)
plt.plot(minsup, zt, label = "Z-Miner", marker = 'o')
plt.plot(minsup, rvt, label = "Z-Miner_RV", marker = 's')
plt.title("CONTEXT (max k = 14, Speedup ≈ 1.4)")
plt.xlabel("Minimum Support")
plt.ylabel("Time (Seconds)")
plt.legend()

#SKATING
minsup = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]
zt = [1975.5625, 1008.625, 468.953125, 280.671875, 183.546875, 122.9375, 64.9375]
rvt = [1819.796875, 947.15625, 442.203125, 268.484375, 173.203125, 111.5625, 63.734375]

plt.subplot(1, 3, 3)
plt.plot(minsup, zt, label = "Z-Miner", marker = 'o')
plt.plot(minsup, rvt, label = "Z-Miner_RV", marker = 's')
plt.title("SKATING (max k = 9, Speedup ≈ 1.07)")
plt.xlabel("Minimum Support")
plt.ylabel("Time (Seconds)")
plt.legend()

plt.show()