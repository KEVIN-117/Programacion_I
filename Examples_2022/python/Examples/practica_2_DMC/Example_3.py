
from datetime import datetime
today = datetime.today()
convertToYearsandMonth = round(10000/365, 2)
years, month = str(convertToYearsandMonth).split(".")
year = (today.year+int(years))
convertDays = 10000-(int(years)*365+int(month)*30)
FutureDate = str(year)+"/"+month+"/"+str(convertDays)
print(FutureDate)
print(years)
print(month)
print(convertDays)
