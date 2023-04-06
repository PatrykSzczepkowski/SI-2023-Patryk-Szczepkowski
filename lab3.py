import numpy as np
import matplotlib.pyplot as plt


years = np.array([2000, 2002, 2005, 2007, 2010])
unemployment = np.array([6.5, 7.0, 7.4, 8.2, 9.0])


years_normalized = (years - years.mean()) / years.std()


m = 0
b = 0


learning_rate = 0.01


iterations = 1000

def cost_function(m, b, years, unemployment):
    n = len(years)
    return (1 / n) * sum((unemployment[i] - (m * years[i] + b))**2 for i in range(n))

def gradient(m, b, years, unemployment):
    n = len(years)
    dm = -(2 / n) * sum(years[i] * (unemployment[i] - (m * years[i] + b)) for i in range(n))
    db = -(2 / n) * sum(unemployment[i] - (m * years[i] + b) for i in range(n))
    return dm, db

for _ in range(iterations):
    dm, db = gradient(m, b, years_normalized, unemployment)
    m -= learning_rate * dm
    b -= learning_rate * db

def linear_regression(rok):
    return m * (rok - years.mean()) / years.std() + b

rok = 2010
while linear_regression(rok) < 12:
    rok += 1

print(f"Model regresji liniowej: y = {m:.3f} * (x - {years.mean():.0f}) / {years.std():.0f} + {b:.3f}")
print(f"Procent bezrobotnych przekroczy 12% w roku {rok}.")

# Wizualizacja modelu regresji liniowej
plt.scatter(years, unemployment, color='blue', label='Dane rzeczywiste')
plt.plot(years, [linear_regression(year) for year in years], color='red', label='Regresja liniowa')
plt.xlabel('Rok')
plt.ylabel('Procent bezrobotnych')
plt.legend()
plt.show()
