#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy import signal


# In[2]:


x = np.arange(-10, 10.1, 0.1)
y = x**2 + 5

plt.figure(figsize= (12,8), dpi= 200)
plt.plot(x, y)
plt.savefig("Zadanie1.png")


# In[3]:


x = np.arange(0, (2 + 1/32)*math.pi, math.pi/32)
sin_y = np.sin(x)
cos_y = np.cos(x)

plt.figure(figsize= (12,8), dpi= 200)
plt.plot(x, sin_y)
plt.plot(x, cos_y, color="red")
plt.savefig("Zadanie2.png")


# In[4]:


t = np.arange(0, 5.01, 0.01)
y = 2 * np.sin(t * 2 * math.pi)
# Nie trzeba mnożyć t przez 1000, ponieważ skala x, jest o 1000 także powiększona

plt.figure(figsize=(12,8), dpi= 200)
plt.plot(t, y)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.savefig("Zadanie3.png")


# In[5]:


t = np.arange(0, 5.01, 0.01)
y1 = 2 * np.cos(t * 2 * math.pi)
y2 = 2 * signal.square(t * 2 * math.pi)
y3 = 2 * signal.sawtooth(t * 2 * math.pi, 0.5)
y4 = 2 * signal.sawtooth(t * 2 * math.pi)

plt.figure(figsize=(12,8), dpi= 200)
plt.plot(t, y1, "red")
plt.plot(t, y2, "green")
plt.plot(t, y3, "black")
plt.plot(t, y4, "blue")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.savefig("Zadanie4.png")