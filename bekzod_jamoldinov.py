# -*- coding: utf-8 -*-
"""Bekzod Jamoldinov

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CAUILQ3uXmX81PAe96DjH8U6LpWHCzfl
"""

import pandas as pd
# 1. DataFrame yaratish
data = {
    'ism': ['Bekzod', 'Abdurahmon', 'Ortiqmirzo', 'Boburjon', 'Shohijahon', 'Samandar','Asadbek', 'Bilolidin', 'Izatbek','Sunatbek','Jamshidbek'],
    'yoshi':[25, 30, 24, 25, 20, 21, 23, 26, 19, 22,19],
    'shahar':['Andijon', 'Uchkoprik','Buxoro','Namangan', 'Navoiy','Qoqon','Fargona','Fargona','Toshkent','Beshariq', 'Fargona']
}
mb= pd.DataFrame(data)
# 2.Malumotlarni korish
print(mb)
# 3.Filtrlash
young_people = mb[mb['yoshi']<25]
print("25 yoshdan kichiklar:\n", young_people)
# 4. Ozgartrish
mb['yoshi']+=1 # har bir shaxsning yoshni 1 ga oshirish
print("yangilangan DataFram:\n",mb)
#5. Manzil
manzil = mb[mb['shahar']=='Fargona']
print("manzil Fargona bolganlar :\n",manzil)

import numpy as np
# 1. massiv yaratish

array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# 2. Matematik operatsiyalar
yigindi_array = np.sum(array_1d)
ortachaqiymat_array = np.mean(array_1d)
kopaytma_array = np.prod(array_1d)

print("1d Massiv: ", array_1d)
print("2d Massiv:\n ", array_2d)
print("Massivlar yig'indisi: ", yigindi_array)
print("O'rtacha qiymat: ", ortachaqiymat_array)
print("Ko'paytma: ", kopaytma_array)