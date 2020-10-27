import matplotlib.pyplot as plt
import numpy as np
import math

# Wartość sygnału kosinusoidalnego dla argumentu.
def cosinusoidal(x :float, A: float, T :float) -> float:
    return A * math.cos(2*math.pi / T * x)

# Wartość sygnału prostokątnego dla argumentu.
def rectangular(x :float, A: float, T :float) -> float:
    periods = math.trunc(x / T) # ile całych okresów jest między 0 i x
    # x - periods * period # x przesunięty do pierwszego okresu
    if x - periods * T < T / 2: # x jest w pierwszej połowie okresu
        return A
    else: # x jest w połowie okresu lub w drugiej połowie okresu
        return -A

# Wartość sygnału trójkątnego dla argumentu.
def triangular(x :float, A: float, T :float) -> float:
    a = A / (T / 4) # współczynnik kierunkowy prostej
    periods = math.trunc(x / T)
    xInPeriod = x - periods * T
    if xInPeriod < T/4: # x jest w 1. ćwiartce okresu
        return a * xInPeriod
    elif xInPeriod < T/2: # x jest w 2. ćwiartce okresu
        return -a * xInPeriod + 2*A
    elif xInPeriod < 3*T/4: # x jest w 3. ćwiartce okresu
        return -a * xInPeriod + 2*A
    else: # x jest w 4. ćwiartce okresu
        return a * xInPeriod - 4*A

# Wartość sygnału piłokształtnego dla argumentu.
def sawtooth(x :float, A: float, T :float) -> float:
    a = A / T # współczynnik kierunkowy prostej
    periods = math.trunc(x / T) # ile całych okresów jest między 0 i x
    return a * (x - periods * T)

signals = (
    (cosinusoidal, 'kosinusoidalny'),
    (rectangular, 'prostokątny'),
    (triangular, 'trójkątny'),
    (sawtooth, 'piłokształtny')
)

start = 0
stop = 5
A = 2
T = 1
for s in signals:
    plt.figure()
    # plt.subplot()
    plt.xlabel('t [ms]')
    plt.ylabel('U [V]')
    plt.title(s[1])
    plt.grid()

    X = np.arange(start, stop, 0.001)
    Y = np.empty(len(X), dtype=float)
    i = 0
    while i < len(Y):
        Y[i] = s[0](X[i], A, T)
        i += 1
    plt.plot(X, Y, color='black')

    plt.savefig(s[1] + '.png')
