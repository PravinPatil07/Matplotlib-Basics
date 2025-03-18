# Matplotlib Examples with Pandas and NumPy

## 1. Basic Line Plot with NumPy
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Line Plot with NumPy')
plt.show()
```

---

## 2. Scatter Plot with NumPy (Advanced Arguments)
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 500  # Varying sizes
colors = np.random.rand(50)  # Color mapping

plt.scatter(x, y, s=sizes, c=colors, alpha=0.7, cmap='viridis', edgecolors='black')
plt.colorbar(label='Color Intensity')
plt.xlabel('Random X')
plt.ylabel('Random Y')
plt.title('Advanced Scatter Plot with NumPy')
plt.show()
```

---

## 3. Bar Chart with Pandas (Advanced Arguments)
```python
import pandas as pd
import matplotlib.pyplot as plt

data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [10, 20, 15, 25]}
df = pd.DataFrame(data)
colors = ['blue', 'green', 'red', 'purple']

plt.bar(df['Category'], df['Values'], color=colors, edgecolor='black', hatch='/')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Advanced Bar Chart with Pandas')
plt.show()
```

---

## 4. Histogram with NumPy
```python
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.hist(data, bins=30, color='c', edgecolor='black', alpha=0.75, histtype='stepfilled', linewidth=1.5)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with NumPy')
plt.show()
```

---

## 5. Pie Chart with Pandas (Advanced Arguments)
```python
import pandas as pd
import matplotlib.pyplot as plt

data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [40, 30, 20, 10]}
df = pd.DataFrame(data)

explode = (0.1, 0, 0, 0)  # Explode first slice
plt.pie(df['Values'], labels=df['Category'], autopct='%1.1f%%', colors=['gold', 'lightblue', 'lightcoral', 'lightgreen'], startangle=140, explode=explode, shadow=True)
plt.title('Advanced Pie Chart with Pandas')
plt.show()
```

---

## 6. Multiple Subplots with NumPy
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(2, 1, figsize=(6, 8))

ax[0].plot(x, y1, 'r', label='Sine')
ax[0].legend()
ax[0].set_title('Sine Wave')

ax[1].plot(x, y2, 'b', label='Cosine')
ax[1].legend()
ax[1].set_title('Cosine Wave')

plt.tight_layout()
plt.show()
```

---

## 7. Pandas DataFrame Line Plot
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20230101', periods=10)
data = np.random.randn(10, 2)
df = pd.DataFrame(data, index=dates, columns=['A', 'B'])

df.plot(figsize=(8, 5), linestyle='--', marker='o', colormap='coolwarm')
plt.title('Pandas DataFrame Line Plot')
plt.xlabel('Date')
plt.ylabel('Values')
plt.grid()
plt.show()
```

---

## Conclusion
These examples demonstrate how to use **Matplotlib** with **Pandas** and **NumPy** for various types of visualizations. Modify the code to explore more! 🚀

