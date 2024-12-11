import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('data.csv')

X = int(len("Raducanu"))
Y = int(len("Rares Aurelian"))


csv.plot()
plt.show()

subpunct2 = csv.head(X)
subpunct2.plot()
plt.show()

categorii = ["Durata", "Puls"]
subpunct3 = csv.tail(Y)[categorii]
subpunct3.plot()
plt.show()