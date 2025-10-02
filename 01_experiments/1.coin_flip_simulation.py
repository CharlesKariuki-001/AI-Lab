import random
import matplotlib.pyplot as plt

flips = 1000
heads = 0
tails = 0

for _ in range(flips):
    if random.choice(["H", "T"]) == "H":
        heads += 1
    else:
        tails += 1

# Print results
print(f"Heads: {heads}, Tails: {tails}")
print(f"Heads Probability ~ {heads / flips:.2f}")
print(f"Tails Probability ~ {tails / flips:.2f}")

# Plot results
labels = ["Heads", "Tails"]
counts = [heads, tails]

plt.bar(labels, counts, color=["skyblue", "orange"])
plt.title("Coin Flip Simulation")
plt.ylabel("Count")
plt.show()
