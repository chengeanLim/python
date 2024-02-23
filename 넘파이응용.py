import numpy as np

hights = [1.83, 1.76, 1.68, 1.86, .177, .173]
whights = [86, 74, 59, 95, 80, 68]

np_h = np.array(hights)
np_w = np.array(weights)

bmi = np_w/(np_h**2)

print('대상자들의 키:', np_h)
print('대상자들의 몸무게:', np_w  )
print('대상자들의 bmi:')
print(bmi)
