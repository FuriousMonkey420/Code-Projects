import pandas as pd
import requests
import numpy as np

#requests code
requests = requests.get('https://www.google.com')
print(f"\n{requests.status_code}\n")

#pandas code
snack = input("Enter snack: ")
snack2 = input("Enter snack: ")
snack3 = input("Enter snack: ")

data = {
  "snacks": [snack, snack2, snack3],
  "calories": [20, 210, 430],
  "duration": [30, 40, 45]
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