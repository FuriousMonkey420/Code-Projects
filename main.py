import pandas as pd
import requests
import numpy as np

#requests code
requests = requests.get('https://www.google.com')
print(f"\n{requests.status_code}\n")

#pandas code
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)

#numpy code
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(f"\n{a.ndim}")
print(b.ndim)
print(c.ndim)
print(d.ndim)