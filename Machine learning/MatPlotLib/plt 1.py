import matplotlib.pyplot as plt


days = list(range(1, 6))
week1 = [12, 9.5, 10, 11, 8]
week2 = [11, 12, 10.5, 11, 9]

plt.title("Week grades")
plt.xlabel("Day")
plt.ylabel("Grade")

# plt.plot(days, week1, label="Misha", marker='^')
# plt.plot(days, week2, label="Ivan", marker='>')

plt.bar(days, week1, label="Misha")
plt.bar(days, week2, label="Ivan")

plt.legend()
plt.show()
