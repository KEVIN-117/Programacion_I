import numpy as np
import pandas as pd 
read = pd.read_csv("Examples_2022\python\Examples\practica_2_DMC\Salaries.csv")
print(read)
print("<--------------------------------------------------------------------------------------------------------------------------------------------->")
print(read.head(5))
print(read.info())
print("<--------------------------------------------------------------------------------------------------------------------------------------------->")
#mean = np.sum(read[['BasePay']], axis=0)
BasePay = read[['BasePay']]
print("El promedio es " + str(BasePay.mean()))

# date max

OvertimePay = read[['OvertimePay']]
print("la mayor cantidad de OvertimePay es: " + str(OvertimePay.max()))