import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('data.csv') #am citi documentul/tabelul cu asta

X = int(len("Raducanu")) #am luat lungimea numelui meu
Y = int(len("Rares Aurelian")) #am luat lungimea prenumelui meu

csv.plot() #am plotat primul grafic 
plt.show() #am afisat graficul

subpunct2 = csv.head(X) #am luat primele X valori
subpunct2.plot()
plt.show()

categorii = ["Durata", "Puls"] #am luat coloanele necesare intr-o lista
subpunct3 = csv.tail(Y)[categorii] #am luat ultimele y valori din coloanele alese
subpunct3.plot()
plt.show()